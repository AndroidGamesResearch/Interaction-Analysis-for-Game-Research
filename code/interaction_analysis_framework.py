"""
interaction_analysis_framework.py

Reusable implementation of the seven-step Interaction-Analysis Framework
used in the accompanying empirical study.

The framework evaluates whether the relationship between a binary feature
(r) and a binary outcome (y) differs between a focal context (c) and its
complement (c-bar).

Required inputs
---------------
- A pandas DataFrame
- exposure: binary column coded 0/1
- context: column defining the contextual feature
- context_value: focal value defining stratum c
- outcome: binary column coded 0/1

The implementation reports:
1. Stratum-specific 2 x 2 contingency tables
2. Conditional outcome probabilities
3. Within-stratum probability differences
4. Conditional odds ratios
5. Additive interaction (DDP)
6. Multiplicative interaction (RoR)
7. CI-based additive, multiplicative, and joint classifications

A Haldane-Anscombe correction is applied only when a 2 x 2 table contains
a zero cell.
"""

import numpy as np
import pandas as pd

Z = 1.96

JOINT_PATTERNS = [
    "++", "--", "00",
    "+0", "0+",
    "-0", "0-",
    "+-", "-+"
]


# ================================================================
# 1. STATISTICAL SUPPORT FUNCTIONS
# ================================================================

def safe_div(a, b):
    """Return a / b, or NaN when the denominator is zero."""
    return np.nan if b == 0 else a / b


def se_prob_diff(p1, n1, p2, n2):
    """Standard error of a difference in estimated probabilities."""
    if n1 == 0 or n2 == 0:
        return np.nan

    return np.sqrt(
        (p1 * (1 - p1)) / n1 +
        (p2 * (1 - p2)) / n2
    )


def se_log_or(a, b, c, d):
    """Standard error of a log odds ratio."""
    if 0 in (a, b, c, d):
        return np.nan

    return np.sqrt(
        1 / a + 1 / b + 1 / c + 1 / d
    )


def apply_correction_if_needed(a, b, c, d, correction=0.5):
    """
    Apply a Haldane-Anscombe correction only when a 2 x 2 table
    contains a zero cell.
    """
    if 0 in (a, b, c, d):
        return (
            a + correction,
            b + correction,
            c + correction,
            d + correction,
            True
        )

    return a, b, c, d, False


# ================================================================
# 2. FRAMEWORK STEP 7: CI-BASED CLASSIFICATION
# ================================================================

def classify_ddp(ddp, se):
    """
    Classify additive interaction from the 95% CI for DDP.

    + : CI lies entirely above 0
    - : CI lies entirely below 0
    0 : CI includes 0
    """
    if pd.isna(ddp) or pd.isna(se):
        return "NA"

    low = ddp - Z * se
    high = ddp + Z * se

    if low > 0:
        return "+"
    if high < 0:
        return "-"
    return "0"


def classify_ror(log_ror, se_log_ror):
    """
    Classify multiplicative interaction from the 95% CI for log(RoR).

    + : CI lies entirely above 0, equivalent to RoR CI > 1
    - : CI lies entirely below 0, equivalent to RoR CI < 1
    0 : CI includes 0, equivalent to RoR CI including 1
    """
    if pd.isna(log_ror) or pd.isna(se_log_ror):
        return "NA"

    low = log_ror - Z * se_log_ror
    high = log_ror + Z * se_log_ror

    if low > 0:
        return "+"
    if high < 0:
        return "-"
    return "0"


def joint_pattern(ddp_direction, ror_direction):
    """Combine additive and multiplicative classifications."""
    if "NA" in (ddp_direction, ror_direction):
        return "NA"

    return ddp_direction + ror_direction


def compact_interaction(pattern):
    """
    Convert the full joint pattern to a compact classification.

    + : ++
    - : --
    0 : 00
    M : mixed or scale-specific evidence
    """
    if pattern == "++":
        return "+"
    if pattern == "--":
        return "-"
    if pattern == "00":
        return "0"
    if pattern == "NA":
        return "NA"
    return "M"


# ================================================================
# 3. INPUT VALIDATION
# ================================================================

def _validate_inputs(data, exposure, context, context_value, outcome):
    """Validate the columns and binary variables required by the framework."""
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame.")

    required = [exposure, context, outcome]
    missing = [column for column in required if column not in data.columns]

    if missing:
        raise ValueError(
            "Missing required column(s): " + ", ".join(missing)
        )

    if data[context].isna().any():
        raise ValueError(
            f"Context column '{context}' contains missing values. "
            "Handle missing context values before running the framework."
        )

    if context_value not in set(data[context].unique()):
        raise ValueError(
            f"context_value={context_value!r} was not found in "
            f"column '{context}'."
        )

    for column in (exposure, outcome):
        nonmissing = data[column].dropna()

        if nonmissing.empty:
            raise ValueError(f"Column '{column}' contains no usable values.")

        values = set(nonmissing.unique())

        if not values.issubset({0, 1, False, True}):
            raise ValueError(
                f"Column '{column}' must be binary and coded 0/1."
            )

        if data[column].isna().any():
            raise ValueError(
                f"Column '{column}' contains missing values. "
                "Handle missing values before running the framework."
            )


# ================================================================
# 4. FRAMEWORK STEP 1: BUILD ONE 2 x 2 TABLE
# ================================================================

def build_2x2(data, exposure, outcome):
    """
    Construct a 2 x 2 table for binary exposure r and binary outcome y.

                    r = 1    r = 0
        y = 1         a        c
        y = 0         b        d
    """
    a = int(((data[exposure] == 1) & (data[outcome] == 1)).sum())
    b = int(((data[exposure] == 1) & (data[outcome] == 0)).sum())
    c = int(((data[exposure] == 0) & (data[outcome] == 1)).sum())
    d = int(((data[exposure] == 0) & (data[outcome] == 0)).sum())

    table = pd.DataFrame(
        {
            f"{exposure}=1 (r)": [a, b],
            f"{exposure}=0 (r-bar)": [c, d]
        },
        index=[
            f"{outcome}=1 (y)",
            f"{outcome}=0 (y-bar)"
        ]
    )

    table["Total"] = table.sum(axis=1)
    table.loc["Total"] = table.sum(axis=0)

    return table, (a, b, c, d)


# ================================================================
# 5. SEVEN-STEP INTERACTION-ANALYSIS FRAMEWORK
# ================================================================

def interaction_analysis(
    data,
    exposure,
    context,
    context_value,
    outcome,
    correction=0.5
):
    """
    Apply the seven-step Interaction-Analysis Framework.

    Parameters
    ----------
    data : pandas.DataFrame
        Dataset on which the interaction is estimated.

    exposure : str
        Binary feature r, coded 0/1.

    context : str
        Column containing the contextual feature c.

    context_value : object
        Focal value of `context`. Observations with this value form
        stratum c; all other values form stratum c-bar.

    outcome : str
        Binary outcome y, coded 0/1.

    correction : float, default=0.5
        Haldane-Anscombe correction applied to all four cells of a
        stratum-specific table only when at least one cell equals zero.

    Returns
    -------
    dict
        Complete seven-step results, including contingency tables,
        probabilities, probability differences, odds ratios, DDP,
        RoR, confidence intervals, and interaction classifications.
    """
    _validate_inputs(
        data,
        exposure,
        context,
        context_value,
        outcome
    )

    focal = data[data[context] == context_value].copy()
    rest = data[data[context] != context_value].copy()

    if focal.empty:
        raise ValueError("The focal context stratum contains no observations.")

    if rest.empty:
        raise ValueError(
            "The complementary context stratum contains no observations."
        )

    # ------------------------------------------------------------
    # FRAMEWORK STEP 1:
    # Construct stratum-specific 2 x 2 contingency tables
    # ------------------------------------------------------------

    focal_table, focal_cells = build_2x2(
        focal,
        exposure,
        outcome
    )

    rest_table, rest_cells = build_2x2(
        rest,
        exposure,
        outcome
    )

    a1, b1, c1, d1 = focal_cells
    a0, b0, c0, d0 = rest_cells

    # ------------------------------------------------------------
    # FRAMEWORK STEP 2:
    # Estimate conditional outcome probabilities
    # ------------------------------------------------------------

    n_r_c = a1 + b1
    n_rbar_c = c1 + d1

    n_r_cbar = a0 + b0
    n_rbar_cbar = c0 + d0

    p_y_r_c = safe_div(a1, n_r_c)
    p_y_rbar_c = safe_div(c1, n_rbar_c)

    p_y_r_cbar = safe_div(a0, n_r_cbar)
    p_y_rbar_cbar = safe_div(c0, n_rbar_cbar)

    # ------------------------------------------------------------
    # FRAMEWORK STEP 3:
    # Assess within-stratum differences in proportions
    # ------------------------------------------------------------

    dp_c = p_y_r_c - p_y_rbar_c
    dp_cbar = p_y_r_cbar - p_y_rbar_cbar

    se_dp_c = se_prob_diff(
        p_y_r_c,
        n_r_c,
        p_y_rbar_c,
        n_rbar_c
    )

    se_dp_cbar = se_prob_diff(
        p_y_r_cbar,
        n_r_cbar,
        p_y_rbar_cbar,
        n_rbar_cbar
    )

    dp_c_low = dp_c - Z * se_dp_c
    dp_c_high = dp_c + Z * se_dp_c

    dp_cbar_low = dp_cbar - Z * se_dp_cbar
    dp_cbar_high = dp_cbar + Z * se_dp_cbar

    # ------------------------------------------------------------
    # FRAMEWORK STEP 4:
    # Estimate conditional odds ratios
    # ------------------------------------------------------------

    A1, B1, C1, D1, corrected_c = apply_correction_if_needed(
        a1, b1, c1, d1, correction
    )

    A0, B0, C0, D0, corrected_cbar = apply_correction_if_needed(
        a0, b0, c0, d0, correction
    )

    or_c = safe_div(A1 * D1, B1 * C1)
    or_cbar = safe_div(A0 * D0, B0 * C0)

    log_or_c = np.log(or_c)
    log_or_cbar = np.log(or_cbar)

    se_log_or_c = se_log_or(A1, B1, C1, D1)
    se_log_or_cbar = se_log_or(A0, B0, C0, D0)

    or_c_low = np.exp(log_or_c - Z * se_log_or_c)
    or_c_high = np.exp(log_or_c + Z * se_log_or_c)

    or_cbar_low = np.exp(log_or_cbar - Z * se_log_or_cbar)
    or_cbar_high = np.exp(log_or_cbar + Z * se_log_or_cbar)

    # ------------------------------------------------------------
    # FRAMEWORK STEP 5:
    # Evaluate additive interaction using DDP
    # ------------------------------------------------------------

    ddp = dp_c - dp_cbar

    se_ddp = np.sqrt(
        se_dp_c**2 +
        se_dp_cbar**2
    )

    ddp_low = ddp - Z * se_ddp
    ddp_high = ddp + Z * se_ddp

    ddp_direction = classify_ddp(
        ddp,
        se_ddp
    )

    # ------------------------------------------------------------
    # FRAMEWORK STEP 6:
    # Evaluate multiplicative interaction using RoR
    # ------------------------------------------------------------

    ror = safe_div(
        or_c,
        or_cbar
    )

    log_ror = np.log(ror)

    se_log_ror = np.sqrt(
        se_log_or_c**2 +
        se_log_or_cbar**2
    )

    log_ror_low = log_ror - Z * se_log_ror
    log_ror_high = log_ror + Z * se_log_ror

    ror_low = np.exp(log_ror_low)
    ror_high = np.exp(log_ror_high)

    ror_direction = classify_ror(
        log_ror,
        se_log_ror
    )

    # ------------------------------------------------------------
    # FRAMEWORK STEP 7:
    # Joint CI-based interpretation
    # ------------------------------------------------------------

    joint = joint_pattern(
        ddp_direction,
        ror_direction
    )

    interaction = compact_interaction(
        joint
    )

    return {
        "exposure": exposure,
        "context": context,
        "context_value": context_value,
        "outcome": outcome,

        "focal_table": focal_table,
        "complement_table": rest_table,

        "cells_c": focal_cells,
        "cells_cbar": rest_cells,

        "p_y_r_c": p_y_r_c,
        "p_y_rbar_c": p_y_rbar_c,
        "p_y_r_cbar": p_y_r_cbar,
        "p_y_rbar_cbar": p_y_rbar_cbar,

        "dp_c": dp_c,
        "dp_c_low": dp_c_low,
        "dp_c_high": dp_c_high,

        "dp_cbar": dp_cbar,
        "dp_cbar_low": dp_cbar_low,
        "dp_cbar_high": dp_cbar_high,

        "or_c": or_c,
        "or_c_low": or_c_low,
        "or_c_high": or_c_high,

        "or_cbar": or_cbar,
        "or_cbar_low": or_cbar_low,
        "or_cbar_high": or_cbar_high,

        "ddp": ddp,
        "ddp_low": ddp_low,
        "ddp_high": ddp_high,
        "ddp_direction": ddp_direction,

        "ror": ror,
        "ror_low": ror_low,
        "ror_high": ror_high,
        "ror_direction": ror_direction,

        "joint_pattern": joint,
        "interaction": interaction,

        "corrected_c": corrected_c,
        "corrected_cbar": corrected_cbar
    }


# ================================================================
# 6. OPTIONAL STRATIFIED APPLICATION
# ================================================================

def interaction_analysis_by(
    data,
    exposure,
    context,
    context_value,
    outcome,
    by,
    correction=0.5
):
    """
    Re-apply the framework independently within one or more grouping
    variables, such as country, month, site, cohort, or period.

    Parameters
    ----------
    by : str or list[str]
        Column(s) defining the strata within which the complete
        interaction framework is re-estimated.

    Returns
    -------
    pandas.DataFrame
        One row per grouping context containing DDP, RoR, confidence
        intervals, full joint pattern, and compact interaction class.
    """
    group_columns = [by] if isinstance(by, str) else list(by)

    missing = [
        column for column in group_columns
        if column not in data.columns
    ]

    if missing:
        raise ValueError(
            "Missing grouping column(s): " + ", ".join(missing)
        )

    rows = []

    grouper = (
        group_columns[0]
        if len(group_columns) == 1
        else group_columns
    )

    for group_key, subset in data.groupby(
        grouper,
        dropna=False,
        sort=True
    ):
        if len(group_columns) == 1:
            group_key = (group_key,)

        row = dict(zip(group_columns, group_key))

        try:
            result = interaction_analysis(
                data=subset,
                exposure=exposure,
                context=context,
                context_value=context_value,
                outcome=outcome,
                correction=correction
            )

            row.update({
                "DDP": result["ddp"],
                "DDP_CI_low": result["ddp_low"],
                "DDP_CI_high": result["ddp_high"],
                "DDP_direction": result["ddp_direction"],
                "RoR": result["ror"],
                "RoR_CI_low": result["ror_low"],
                "RoR_CI_high": result["ror_high"],
                "RoR_direction": result["ror_direction"],
                "joint_pattern": result["joint_pattern"],
                "interaction": result["interaction"]
            })

        except (ValueError, ZeroDivisionError, FloatingPointError):
            row.update({
                "DDP": np.nan,
                "DDP_CI_low": np.nan,
                "DDP_CI_high": np.nan,
                "DDP_direction": "NA",
                "RoR": np.nan,
                "RoR_CI_low": np.nan,
                "RoR_CI_high": np.nan,
                "RoR_direction": "NA",
                "joint_pattern": "NA",
                "interaction": "NA"
            })

        rows.append(row)

    return pd.DataFrame(rows)


# ================================================================
# 7. COMPACT RESULT SUMMARY
# ================================================================

def summarize_result(result):
    """Return the principal interaction estimates as a one-row DataFrame."""
    return pd.DataFrame([{
        "Exposure": result["exposure"],
        "Context": result["context"],
        "Context value": result["context_value"],
        "Outcome": result["outcome"],
        "DDP": result["ddp"],
        "DDP CI low": result["ddp_low"],
        "DDP CI high": result["ddp_high"],
        "DDP direction": result["ddp_direction"],
        "RoR": result["ror"],
        "RoR CI low": result["ror_low"],
        "RoR CI high": result["ror_high"],
        "RoR direction": result["ror_direction"],
        "Joint pattern": result["joint_pattern"],
        "Interaction": result["interaction"]
    }])


# ================================================================
# EXAMPLE USAGE
# ================================================================
#
# Pooled analysis:
#
# result = interaction_analysis(
#     data=df,
#     exposure="treatment",
#     context="group",
#     context_value="Group A",
#     outcome="success"
# )
#
# print(result["focal_table"])
# print(result["complement_table"])
# print(summarize_result(result))
#
#
# Re-apply the framework by one contextual dimension:
#
# country_results = interaction_analysis_by(
#     data=df,
#     exposure="treatment",
#     context="group",
#     context_value="Group A",
#     outcome="success",
#     by="country"
# )
#
#
# Re-apply the framework by multiple contextual dimensions:
#
# country_month_results = interaction_analysis_by(
#     data=df,
#     exposure="treatment",
#     context="group",
#     context_value="Group A",
#     outcome="success",
#     by=["country", "month"]
# )
