# =====================================================================
# ADS × RPG — WORKED INTERACTION ANALYSIS
# Supplementary reproducibility material
#
# This script generates the complete Ads × RPG worked example used to
# illustrate the Interaction-Analysis Framework in the paper. It
# reproduces the analytical steps, interaction estimates, confidence
# intervals, country- and time-specific results, tables, and figures
# reported in the worked example, allowing readers to verify the
# calculations and resulting empirical evidence.
#
# Output:
#     ads_rpg_worked_example.pdf
# =====================================================================


# =====================================================================
# 0. IMPORTS
# =====================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import textwrap

from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle


# =====================================================================
# 1. ANALYTICAL SETTINGS
# =====================================================================
# Load dataset
apps = pd.read_csv("ads_iap_googlePlayStore_42country_month_panel.csv")
df = apps.copy()

EXPOSURE = "contains_ads"
GENRE = "RPG"

INSTALL = "install_success"
RATING = "rating_success"

OUTPUT_FILE = "ads_rpg_worked_example.pdf"

Z = 1.96

INSTALL_COUNTRIES = {
    "US": "United States",
    "IN": "India"
}

TEMPORAL_COUNTRY = "US"

RATING_COUNTRY = "US"
RATING_COUNTRY_NAME = "United States"


# =====================================================================
# 2. MONTH HANDLING
# =====================================================================

def month_label(value):
    try:
        return pd.to_datetime(value).strftime("%b %Y")
    except Exception:
        return str(value)


available_months = (
    df.loc[df["country"] == TEMPORAL_COUNTRY, "month"]
      .dropna()
      .sort_values()
      .unique()
      .tolist()
)

if len(available_months) < 3:
    raise ValueError("At least three US months are required.")


INSTALL_MONTHS = [
    available_months[0],
    available_months[len(available_months) // 2],
    available_months[-1]
]

# One representative month for the shorter rating example
RATING_MONTH = INSTALL_MONTHS[1]


# =====================================================================
# 3. STATISTICAL HELPERS
# =====================================================================

def safe_div(num, den):
    return np.nan if den == 0 else num / den


def se_probability_difference(p1, n1, p0, n0):
    if n1 == 0 or n0 == 0:
        return np.nan

    return np.sqrt(
        p1 * (1 - p1) / n1
        +
        p0 * (1 - p0) / n0
    )


def zero_cell_correction(a, b, c, d):
    corrected = any(x == 0 for x in [a, b, c, d])

    if corrected:
        return (
            a + 0.5,
            b + 0.5,
            c + 0.5,
            d + 0.5,
            True
        )

    return (
        float(a),
        float(b),
        float(c),
        float(d),
        False
    )


def se_log_or(a, b, c, d):
    return np.sqrt(
        1/a + 1/b + 1/c + 1/d
    )


def classify_ddp(low, high):
    if low > 0:
        return "+"
    if high < 0:
        return "-"
    return "0"


def classify_ror(low, high):
    if low > 1:
        return "+"
    if high < 1:
        return "-"
    return "0"


def get_cells(data, outcome):
    valid = data[
        data[outcome].isin([0, 1])
        &
        data[EXPOSURE].isin([0, 1])
    ].copy()

    a = int(
        (
            (valid[EXPOSURE] == 1)
            &
            (valid[outcome] == 1)
        ).sum()
    )

    b = int(
        (
            (valid[EXPOSURE] == 1)
            &
            (valid[outcome] == 0)
        ).sum()
    )

    c = int(
        (
            (valid[EXPOSURE] == 0)
            &
            (valid[outcome] == 1)
        ).sum()
    )

    d = int(
        (
            (valid[EXPOSURE] == 0)
            &
            (valid[outcome] == 0)
        ).sum()
    )

    return a, b, c, d


# =====================================================================
# 4. COMPLETE INTERACTION CALCULATION
# =====================================================================

def calculate_interaction(data, outcome):

    data = data[
        data[outcome].isin([0, 1])
        &
        data[EXPOSURE].isin([0, 1])
        &
        data["genre"].notna()
    ].copy()

    focal = data[data["genre"] == GENRE].copy()
    other = data[data["genre"] != GENRE].copy()

    if len(focal) == 0:
        raise ValueError("No RPG observations in this context.")

    if len(other) == 0:
        raise ValueError("No non-RPG observations in this context.")

    # -----------------------------------------------------------------
    # 2 × 2 cells
    # -----------------------------------------------------------------

    a1, b1, c1, d1 = get_cells(focal, outcome)
    a0, b0, c0, d0 = get_cells(other, outcome)

    # -----------------------------------------------------------------
    # Conditional probabilities
    # -----------------------------------------------------------------

    p_r_ads = safe_div(a1, a1 + b1)
    p_r_noads = safe_div(c1, c1 + d1)

    p_n_ads = safe_div(a0, a0 + b0)
    p_n_noads = safe_div(c0, c0 + d0)

    # -----------------------------------------------------------------
    # Probability differences
    # -----------------------------------------------------------------

    dp_r = p_r_ads - p_r_noads
    dp_n = p_n_ads - p_n_noads

    se_dp_r = se_probability_difference(
        p_r_ads, a1 + b1,
        p_r_noads, c1 + d1
    )

    se_dp_n = se_probability_difference(
        p_n_ads, a0 + b0,
        p_n_noads, c0 + d0
    )

    dp_r_low = dp_r - Z * se_dp_r
    dp_r_high = dp_r + Z * se_dp_r

    dp_n_low = dp_n - Z * se_dp_n
    dp_n_high = dp_n + Z * se_dp_n

    # -----------------------------------------------------------------
    # Odds ratios
    # -----------------------------------------------------------------

    A1, B1, C1, D1, correction_rpg = zero_cell_correction(
        a1, b1, c1, d1
    )

    A0, B0, C0, D0, correction_nonrpg = zero_cell_correction(
        a0, b0, c0, d0
    )

    OR_r = (A1 * D1) / (B1 * C1)
    OR_n = (A0 * D0) / (B0 * C0)

    log_OR_r = np.log(OR_r)
    log_OR_n = np.log(OR_n)

    se_log_OR_r = se_log_or(A1, B1, C1, D1)
    se_log_OR_n = se_log_or(A0, B0, C0, D0)

    OR_r_low = np.exp(log_OR_r - Z * se_log_OR_r)
    OR_r_high = np.exp(log_OR_r + Z * se_log_OR_r)

    OR_n_low = np.exp(log_OR_n - Z * se_log_OR_n)
    OR_n_high = np.exp(log_OR_n + Z * se_log_OR_n)

    # -----------------------------------------------------------------
    # Additive interaction
    # -----------------------------------------------------------------

    DDP = dp_r - dp_n

    se_DDP = np.sqrt(
        se_dp_r**2
        +
        se_dp_n**2
    )

    DDP_low = DDP - Z * se_DDP
    DDP_high = DDP + Z * se_DDP

    DDP_direction = classify_ddp(
        DDP_low,
        DDP_high
    )

    # -----------------------------------------------------------------
    # Multiplicative interaction
    # -----------------------------------------------------------------

    RoR = OR_r / OR_n
    log_RoR = np.log(RoR)

    se_log_RoR = np.sqrt(
        se_log_OR_r**2
        +
        se_log_OR_n**2
    )

    log_RoR_low = log_RoR - Z * se_log_RoR
    log_RoR_high = log_RoR + Z * se_log_RoR

    RoR_low = np.exp(log_RoR_low)
    RoR_high = np.exp(log_RoR_high)

    RoR_direction = classify_ror(
        RoR_low,
        RoR_high
    )

    joint = DDP_direction + RoR_direction

    # -----------------------------------------------------------------
    # Odds / log odds for plots
    # -----------------------------------------------------------------

    odds_r_noads = safe_div(
        p_r_noads,
        1 - p_r_noads
    )

    odds_r_ads = safe_div(
        p_r_ads,
        1 - p_r_ads
    )

    odds_n_noads = safe_div(
        p_n_noads,
        1 - p_n_noads
    )

    odds_n_ads = safe_div(
        p_n_ads,
        1 - p_n_ads
    )

    eps = 1e-12

    log_odds_r_noads = np.log(
        max(odds_r_noads, eps)
    )

    log_odds_r_ads = np.log(
        max(odds_r_ads, eps)
    )

    log_odds_n_noads = np.log(
        max(odds_n_noads, eps)
    )

    log_odds_n_ads = np.log(
        max(odds_n_ads, eps)
    )

    return {

        "n": len(data),

        # RPG cells
        "a1": a1,
        "b1": b1,
        "c1": c1,
        "d1": d1,

        # Non-RPG cells
        "a0": a0,
        "b0": b0,
        "c0": c0,
        "d0": d0,

        # probabilities
        "p_r_ads": p_r_ads,
        "p_r_noads": p_r_noads,

        "p_n_ads": p_n_ads,
        "p_n_noads": p_n_noads,

        # probability differences
        "dp_r": dp_r,
        "dp_r_low": dp_r_low,
        "dp_r_high": dp_r_high,

        "dp_n": dp_n,
        "dp_n_low": dp_n_low,
        "dp_n_high": dp_n_high,

        # OR
        "OR_r": OR_r,
        "OR_r_low": OR_r_low,
        "OR_r_high": OR_r_high,

        "OR_n": OR_n,
        "OR_n_low": OR_n_low,
        "OR_n_high": OR_n_high,

        "log_OR_r": log_OR_r,
        "log_OR_n": log_OR_n,

        # DDP
        "DDP": DDP,
        "DDP_low": DDP_low,
        "DDP_high": DDP_high,
        "DDP_direction": DDP_direction,

        # RoR
        "RoR": RoR,
        "RoR_low": RoR_low,
        "RoR_high": RoR_high,

        "log_RoR": log_RoR,
        "log_RoR_low": log_RoR_low,
        "log_RoR_high": log_RoR_high,

        "RoR_direction": RoR_direction,

        "joint": joint,

        # odds
        "odds_r_noads": odds_r_noads,
        "odds_r_ads": odds_r_ads,

        "odds_n_noads": odds_n_noads,
        "odds_n_ads": odds_n_ads,

        # log odds
        "log_odds_r_noads": log_odds_r_noads,
        "log_odds_r_ads": log_odds_r_ads,

        "log_odds_n_noads": log_odds_n_noads,
        "log_odds_n_ads": log_odds_n_ads,

        "correction_rpg": correction_rpg,
        "correction_nonrpg": correction_nonrpg
    }


# =====================================================================
# 5. CALCULATE ALL RESULTS
# =====================================================================

install_pooled = calculate_interaction(
    df,
    INSTALL
)

install_countries = {}

for code, name in INSTALL_COUNTRIES.items():

    subset = df[
        df["country"] == code
    ].copy()

    install_countries[name] = calculate_interaction(
        subset,
        INSTALL
    )


install_months = {}

for month in INSTALL_MONTHS:

    subset = df[
        (df["country"] == TEMPORAL_COUNTRY)
        &
        (df["month"] == month)
    ].copy()

    install_months[
        month_label(month)
    ] = calculate_interaction(
        subset,
        INSTALL
    )


rating_pooled = calculate_interaction(
    df,
    RATING
)


rating_us = calculate_interaction(

    df[
        df["country"] == RATING_COUNTRY
    ].copy(),

    RATING
)


rating_month = calculate_interaction(

    df[
        (df["country"] == RATING_COUNTRY)
        &
        (df["month"] == RATING_MONTH)
    ].copy(),

    RATING
)


# =====================================================================
# 6. PUBLICATION TYPOGRAPHY
# =====================================================================

mpl.rcParams.update({

    # Body
    "font.family": "serif",

    # Use fonts normally available with Matplotlib.
    # The first available font will be selected.
    "font.serif": [
        "STIXGeneral",
        "DejaVu Serif",
        "Times New Roman",
        "Times"
    ],

    "mathtext.fontset": "stix",

    "font.size": 8.4,

    # Axes
    "axes.titlesize": 9.0,
    "axes.titleweight": "normal",

    "axes.labelsize": 7.8,

    "axes.linewidth": 0.55,

    # ticks
    "xtick.labelsize": 7.0,
    "ytick.labelsize": 7.0,

    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,

    "xtick.major.size": 3,
    "ytick.major.size": 3,

    # legend
    "legend.fontsize": 7.0,

    # save
    "savefig.dpi": 300,

    # PDF
    "pdf.fonttype": 42,
    "ps.fonttype": 42
})


# =====================================================================
# 7. DESIGN TOKENS
# =====================================================================

INK = "0.10"

TEXT = "0.18"

MUTED = "0.40"

RULE = "0.70"

LIGHT_RULE = "0.86"

PALE = "0.955"

VERY_PALE = "0.985"

DARK_BAR = "0.24"

MID_BAR = "0.56"

LIGHT_BAR = "0.76"

WHITE = "1.0"


# A4 margins
LEFT = 0.090
RIGHT = 0.910
WIDTH = RIGHT - LEFT


# =====================================================================
# 8. GENERAL PAGE HELPERS
# =====================================================================

def new_page():
    fig = plt.figure(
        figsize=(8.27, 11.69),
        facecolor="white"
    )
    return fig


def add_line(
    fig,
    x1,
    x2,
    y,
    color=RULE,
    lw=0.5
):
    fig.lines.append(
        Line2D(
            [x1, x2],
            [y, y],
            transform=fig.transFigure,
            color=color,
            linewidth=lw
        )
    )


def page_header(
    fig,
    title,
    subtitle=None
):

    fig.text(
        LEFT,
        0.956,
        title,
        fontsize=16.0,
        fontweight="bold",
        color=INK,
        ha="left",
        va="top"
    )

    if subtitle:

        fig.text(
            LEFT,
            0.922,
            subtitle,
            fontsize=8.3,
            color=MUTED,
            ha="left",
            va="top"
        )

    add_line(
        fig,
        LEFT,
        RIGHT,
        0.895,
        color=RULE,
        lw=0.55
    )


def page_footer(
    fig,
    page_number
):

    add_line(
        fig,
        LEFT,
        RIGHT,
        0.045,
        color=LIGHT_RULE,
        lw=0.45
    )

    fig.text(
        LEFT,
        0.026,
        "Supplementary worked example  |  Ads × RPG interaction analysis",
        fontsize=5.9,
        color=MUTED,
        ha="left"
    )

    fig.text(
        RIGHT,
        0.026,
        str(page_number),
        fontsize=6.0,
        color=MUTED,
        ha="right"
    )


def section_heading(
    fig,
    y,
    number,
    title
):

    if number is not None:

        fig.text(
            LEFT,
            y,
            str(number),
            fontsize=7.2,
            fontweight="bold",
            color=MUTED,
            ha="left",
            va="top"
        )

        title_x = LEFT + 0.035

    else:

        title_x = LEFT

    fig.text(
        title_x,
        y,
        title,
        fontsize=10.0,
        fontweight="bold",
        color=INK,
        ha="left",
        va="top"
    )

    add_line(
        fig,
        LEFT,
        RIGHT,
        y - 0.022,
        color=LIGHT_RULE,
        lw=0.45
    )


def caption(
    fig,
    y,
    label,
    text
):

    fig.text(
        LEFT,
        y,
        label,
        fontsize=6.8,
        fontweight="bold",
        color=TEXT,
        va="top"
    )

    fig.text(
        LEFT + 0.075,
        y,
        text,
        fontsize=6.8,
        color=MUTED,
        va="top",
        wrap=True
    )


def note(
    fig,
    x,
    y,
    text,
    width=100,
    fontsize=7.3
):

    wrapped = "\n".join(
        textwrap.wrap(
            text,
            width=width
        )
    )

    fig.text(
        x,
        y,
        wrapped,
        fontsize=fontsize,
        color=TEXT,
        ha="left",
        va="top",
        linespacing=1.38
    )


# =====================================================================
# 9. BOOKTABS-STYLE TABLE
# =====================================================================

def publication_table(
    fig,
    rect,
    rows,
    columns,
    col_widths=None,
    fontsize=7.4,
    header_fontsize=None,
    row_height=1.35,
    first_col_bold=False,
    alignments=None
):

    ax = fig.add_axes(rect)

    ax.axis("off")

    if header_fontsize is None:
        header_fontsize = fontsize

    if col_widths is None:
        col_widths = [
            1 / len(columns)
        ] * len(columns)

    table = ax.table(
        cellText=rows,
        colLabels=columns,
        cellLoc="center",
        colLoc="center",
        colWidths=col_widths,
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(fontsize)
    table.scale(1, row_height)

    cells = table.get_celld()

    nrows = len(rows) + 1
    ncols = len(columns)

    # Remove spreadsheet-style boxes
    for (r, c), cell in cells.items():

        cell.set_facecolor(WHITE)
        cell.set_edgecolor(WHITE)
        cell.set_linewidth(0)

        cell.PAD = 0.04

        if r == 0:

            cell.set_text_props(
                fontweight="bold",
                fontsize=header_fontsize,
                color=INK
            )

        else:

            cell.set_text_props(
                color=TEXT
            )

            if first_col_bold and c == 0:
                cell.set_text_props(
                    fontweight="bold",
                    color=INK
                )

        if alignments is not None:

            alignment = alignments[c]

            cell.get_text().set_ha(
                alignment
            )

    # Need canvas positions before drawing booktabs rules
    fig.canvas.draw()

    renderer = fig.canvas.get_renderer()

    # Top of header
    top_bbox = cells[(0, 0)].get_window_extent(renderer)
    top_y = ax.transAxes.inverted().transform(
        (top_bbox.x0, top_bbox.y1)
    )[1]

    # Bottom of header
    header_bbox = cells[(0, 0)].get_window_extent(renderer)
    header_bottom = ax.transAxes.inverted().transform(
        (header_bbox.x0, header_bbox.y0)
    )[1]

    # Bottom of table
    bottom_bbox = cells[(nrows - 1, 0)].get_window_extent(renderer)
    bottom_y = ax.transAxes.inverted().transform(
        (bottom_bbox.x0, bottom_bbox.y0)
    )[1]

    ax.plot(
        [0, 1],
        [top_y, top_y],
        transform=ax.transAxes,
        color=INK,
        linewidth=0.75,
        clip_on=False
    )

    ax.plot(
        [0, 1],
        [header_bottom, header_bottom],
        transform=ax.transAxes,
        color=RULE,
        linewidth=0.45,
        clip_on=False
    )

    ax.plot(
        [0, 1],
        [bottom_y, bottom_y],
        transform=ax.transAxes,
        color=INK,
        linewidth=0.75,
        clip_on=False
    )

    return table


# =====================================================================
# 10. CONTINGENCY TABLE
# =====================================================================

def contingency_booktabs(
    fig,
    rect,
    title,
    a,
    b,
    c,
    d
):

    fig.text(
        rect[0],
        rect[1] + rect[3] + 0.015,
        title,
        fontsize=8.3,
        fontweight="bold",
        color=INK
    )

    rows = [
        [
            "Success",
            f"{a:,}",
            f"{c:,}",
            f"{a+c:,}"
        ],
        [
            "Not success",
            f"{b:,}",
            f"{d:,}",
            f"{b+d:,}"
        ],
        [
            "Total",
            f"{a+b:,}",
            f"{c+d:,}",
            f"{a+b+c+d:,}"
        ]
    ]

    table = publication_table(
        fig,
        rect,
        rows,
        [
            "",
            "Ads = 1",
            "Ads = 0",
            "Total"
        ],
        col_widths=[
            0.31,
            0.23,
            0.23,
            0.23
        ],
        fontsize=7.5,
        row_height=1.42,
        first_col_bold=True
    )

    # Emphasise total row without shading
    for c in range(4):

        table[(3, c)].set_text_props(
            fontweight="bold",
            color=INK
        )


# =====================================================================
# 11. CONDITIONAL PROBABILITY TABLE
# =====================================================================

def probability_booktabs(
    fig,
    rect,
    title,
    a,
    b,
    c,
    d
):

    p_ads = safe_div(a, a+b)
    p_noads = safe_div(c, c+d)

    fig.text(
        rect[0],
        rect[1] + rect[3] + 0.013,
        title,
        fontsize=8.1,
        fontweight="bold",
        color=INK
    )

    rows = [
        [
            "Success",
            f"{a:,} / {a+b:,} = {p_ads:.4f}",
            f"{c:,} / {c+d:,} = {p_noads:.4f}"
        ]
    ]

    publication_table(
        fig,
        rect,
        rows,
        [
            "Outcome",
            "Ads = 1",
            "Ads = 0"
        ],
        col_widths=[
            0.22,
            0.39,
            0.39
        ],
        fontsize=7.4,
        row_height=1.50,
        first_col_bold=True
    )


# =====================================================================
# 12. STANDARD AXIS STYLE
# =====================================================================

def clean_axis(
    ax,
    horizontal_grid=True
):

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.spines["left"].set_color(RULE)
    ax.spines["bottom"].set_color(RULE)

    ax.spines["left"].set_linewidth(0.55)
    ax.spines["bottom"].set_linewidth(0.55)

    ax.tick_params(
        colors=TEXT,
        width=0.5
    )

    if horizontal_grid:

        ax.yaxis.grid(
            True,
            color="0.90",
            linewidth=0.45
        )

        ax.set_axisbelow(True)


# =====================================================================
# 13. ZERO-CENTRED BAR CHART
# =====================================================================

def zero_bar_chart(
    ax,
    labels,
    values,
    ylabel,
    title=None,
    shades=None,
    value_decimals=3
):

    values = np.asarray(values, dtype=float)

    x = np.arange(len(values))

    if shades is None:

        shades = [DARK_BAR] * len(values)

    bars = ax.bar(
        x,
        values,
        width=0.56,
        color=shades,
        edgecolor=INK,
        linewidth=0.45
    )

    ax.axhline(
        0,
        color=INK,
        linewidth=0.85
    )

    span = max(
        np.max(np.abs(values)),
        0.05
    )

    ax.set_ylim(
        -span * 1.30,
        span * 1.30
    )

    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    ax.set_ylabel(ylabel)

    if title:
        ax.set_title(
            title,
            pad=8
        )

    clean_axis(ax)

    for bar, value in zip(
        bars,
        values
    ):

        offset = span * 0.045

        if value >= 0:

            y = value + offset
            va = "bottom"

        else:

            y = value - offset
            va = "top"

        ax.text(
            bar.get_x() + bar.get_width()/2,
            y,
            f"{value:+.{value_decimals}f}",
            ha="center",
            va=va,
            fontsize=6.7,
            color=TEXT
        )


# =====================================================================
# 14. PROBABILITY INTERACTION PLOT
# =====================================================================

def probability_interaction_plot(
    ax,
    R,
    outcome_label
):

    ax.plot(
        [0, 1],
        [
            R["p_r_noads"],
            R["p_r_ads"]
        ],
        color=INK,
        marker="o",
        markersize=4.2,
        linewidth=1.45,
        label="RPG"
    )

    ax.plot(
        [0, 1],
        [
            R["p_n_noads"],
            R["p_n_ads"]
        ],
        color=MID_BAR,
        marker="s",
        markersize=4.0,
        linewidth=1.35,
        linestyle="--",
        label="Non-RPG"
    )

    values = [
        R["p_r_noads"],
        R["p_r_ads"],
        R["p_n_noads"],
        R["p_n_ads"]
    ]

    ymin = max(
        0,
        min(values) - 0.07
    )

    ymax = min(
        1,
        max(values) + 0.07
    )

    ax.set_ylim(
        ymin,
        ymax
    )

    ax.set_xlim(
        -0.08,
        1.08
    )

    ax.set_xticks(
        [0, 1]
    )

    ax.set_xticklabels(
        [
            "Ads absent",
            "Ads present"
        ]
    )

    ax.set_ylabel(
        f"P({outcome_label.lower()})"
    )

    ax.legend(
        frameon=False,
        loc="best",
        handlelength=2.0
    )

    clean_axis(ax)

    for x, y in [
        (0, R["p_r_noads"]),
        (1, R["p_r_ads"]),
        (0, R["p_n_noads"]),
        (1, R["p_n_ads"])
    ]:

        ax.annotate(
            f"{y:.3f}",
            (x, y),
            xytext=(0, 6),
            textcoords="offset points",
            ha="center",
            fontsize=6.3,
            color=MUTED
        )


# =====================================================================
# 15. LOG-ODDS INTERACTION PLOT
# =====================================================================

def log_odds_interaction_plot(
    ax,
    R,
    outcome_label
):

    ax.plot(
        [0, 1],
        [
            R["log_odds_r_noads"],
            R["log_odds_r_ads"]
        ],
        color=INK,
        marker="o",
        markersize=4.2,
        linewidth=1.45,
        label="RPG"
    )

    ax.plot(
        [0, 1],
        [
            R["log_odds_n_noads"],
            R["log_odds_n_ads"]
        ],
        color=MID_BAR,
        marker="s",
        markersize=4.0,
        linewidth=1.35,
        linestyle="--",
        label="Non-RPG"
    )

    values = [
        R["log_odds_r_noads"],
        R["log_odds_r_ads"],
        R["log_odds_n_noads"],
        R["log_odds_n_ads"]
    ]

    span = max(values) - min(values)

    margin = max(
        span * 0.10,
        0.12
    )

    ax.set_ylim(
        min(values) - margin,
        max(values) + margin
    )

    ax.set_xlim(
        -0.08,
        1.08
    )

    ax.set_xticks(
        [0, 1]
    )

    ax.set_xticklabels(
        [
            "Ads absent",
            "Ads present"
        ]
    )

    ax.set_ylabel(
        f"Log odds of {outcome_label.lower()}"
    )

    ax.legend(
        frameon=False,
        loc="best",
        handlelength=2.0
    )

    clean_axis(ax)

    for x, y in [
        (0, R["log_odds_r_noads"]),
        (1, R["log_odds_r_ads"]),
        (0, R["log_odds_n_noads"]),
        (1, R["log_odds_n_ads"])
    ]:

        ax.annotate(
            f"{y:+.2f}",
            (x, y),
            xytext=(0, 6),
            textcoords="offset points",
            ha="center",
            fontsize=6.3,
            color=MUTED
        )


# =====================================================================
# 16. CONTEXT RESULT TABLE
# =====================================================================

def context_results_table(
    fig,
    rect,
    contexts
):

    rows = []

    for label, R in contexts.items():

        rows.append([
            label,
            f"{R['dp_r']:+.3f}",
            f"{R['dp_n']:+.3f}",
            f"{R['DDP']:+.3f}",
            f"{R['OR_r']:.3f}",
            f"{R['OR_n']:.3f}",
            f"{R['RoR']:.3f}",
            R["joint"]
        ])

    publication_table(
        fig,
        rect,
        rows,
        [
            "Context",
            "RPG\nΔp",
            "Non-RPG\nΔp",
            "DDP",
            "RPG\nOR",
            "Non-RPG\nOR",
            "RoR",
            "Joint"
        ],
        col_widths=[
            0.20,
            0.105,
            0.12,
            0.105,
            0.105,
            0.12,
            0.105,
            0.04
        ],
        fontsize=6.7,
        header_fontsize=6.4,
        row_height=1.45,
        first_col_bold=True
    )


# =====================================================================
# 17. CONTEXT CALCULATION BLOCK
#
# Cleaner replacement for the old "tiny table + tiny equations" block.
# =====================================================================

def context_calculation_block(
    fig,
    R,
    title,
    y_top
):

    # title
    fig.text(
        LEFT + 0.020,
        y_top,
        title,
        fontsize=9.0,
        fontweight="bold",
        color=INK,
        va="top"
    )

    # thin contextual rule
    add_line(
        fig,
        LEFT + 0.020,
        RIGHT - 0.020,
        y_top - 0.023,
        color=LIGHT_RULE,
        lw=0.40
    )

    # --------------------------------------------------------------
    # Left: compact cell-count table
    # --------------------------------------------------------------

    rows = [
        [
            "RPG",
            f"{R['a1']:,}",
            f"{R['b1']:,}",
            f"{R['c1']:,}",
            f"{R['d1']:,}"
        ],
        [
            "Non-RPG",
            f"{R['a0']:,}",
            f"{R['b0']:,}",
            f"{R['c0']:,}",
            f"{R['d0']:,}"
        ]
    ]

    publication_table(
        fig,
        [
            LEFT + 0.020,
            y_top - 0.150,
            0.39,
            0.105
        ],
        rows,
        [
            "Stratum",
            "Ads+\nSuccess",
            "Ads+\nNo",
            "Ads−\nSuccess",
            "Ads−\nNo"
        ],
        col_widths=[
            0.22,
            0.195,
            0.195,
            0.195,
            0.195
        ],
        fontsize=6.5,
        header_fontsize=6.1,
        row_height=1.35,
        first_col_bold=True
    )

    # --------------------------------------------------------------
    # Right: aligned calculation sequence
    # --------------------------------------------------------------

    x = 0.535

    fig.text(
        x,
        y_top - 0.050,
        (
            r"$\Delta p_{\mathrm{RPG}}"
            rf"={R['p_r_ads']:.4f}"
            rf"-{R['p_r_noads']:.4f}"
            rf"={R['dp_r']:+.4f}$"
        ),
        fontsize=7.8,
        color=TEXT
    )

    fig.text(
        x,
        y_top - 0.083,
        (
            r"$\Delta p_{\mathrm{Non\!-\!RPG}}"
            rf"={R['p_n_ads']:.4f}"
            rf"-{R['p_n_noads']:.4f}"
            rf"={R['dp_n']:+.4f}$"
        ),
        fontsize=7.8,
        color=TEXT
    )

    fig.text(
        x,
        y_top - 0.120,
        (
            r"$\mathrm{DDP}"
            rf"={R['dp_r']:+.4f}"
            rf"-({R['dp_n']:+.4f})"
            rf"=\mathbf{{{R['DDP']:+.4f}}}$"
        ),
        fontsize=8.1,
        color=INK
    )

    fig.text(
        x,
        y_top - 0.157,
        (
            r"$\mathrm{RoR}"
            rf"={R['OR_r']:.4f}"
            rf"/{R['OR_n']:.4f}"
            rf"=\mathbf{{{R['RoR']:.4f}}}$"
        ),
        fontsize=8.1,
        color=INK
    )

    fig.text(
        0.835,
        y_top - 0.157,
        f"Joint: {R['joint']}",
        fontsize=7.4,
        fontweight="bold",
        color=TEXT
    )


# =====================================================================
# 18. TWO-PANEL CONTEXT SUMMARY
# =====================================================================

def context_summary_figure(
    fig,
    contexts,
    rect_left,
    rect_right,
    short_labels=None
):

    labels = list(contexts.keys())

    if short_labels is None:
        plot_labels = labels
    else:
        plot_labels = short_labels

    ddp = np.array([
        contexts[k]["DDP"]
        for k in labels
    ])

    log_ror = np.array([
        contexts[k]["log_RoR"]
        for k in labels
    ])

    # --------------------------------------------------------------
    # DDP
    # --------------------------------------------------------------

    ax1 = fig.add_axes(rect_left)

    zero_bar_chart(
        ax1,
        plot_labels,
        ddp,
        "DDP",
        title="Additive interaction"
    )

    # --------------------------------------------------------------
    # log(RoR)
    # --------------------------------------------------------------

    ax2 = fig.add_axes(rect_right)

    zero_bar_chart(
        ax2,
        plot_labels,
        log_ror,
        "log(RoR)",
        title="Multiplicative interaction",
        shades=[MID_BAR] * len(labels)
    )


# =====================================================================
# PAGE 1
# POOLED INSTALL: DATA CONSTRUCTION
# =====================================================================

def render_page_1(pdf):

    R = install_pooled

    fig = new_page()

    page_header(
        fig,
        "Worked example: Ads × RPG interaction",
        "Outcome 1 — Install success  |  Pooled analysis"
    )

    section_heading(
        fig,
        0.855,
        "1",
        "Construct the two exposure-by-outcome tables"
    )

    contingency_booktabs(
        fig,
        [0.13, 0.675, 0.74, 0.115],
        f"RPG stratum  (n = {R['a1']+R['b1']+R['c1']+R['d1']:,})",
        R["a1"], R["b1"], R["c1"], R["d1"]
    )

    contingency_booktabs(
        fig,
        [0.13, 0.495, 0.74, 0.115],
        f"Non-RPG stratum  (n = {R['a0']+R['b0']+R['c0']+R['d0']:,})",
        R["a0"], R["b0"], R["c0"], R["d0"]
    )

    section_heading(
        fig,
        0.420,
        "2",
        "Estimate conditional success probabilities"
    )

    probability_booktabs(
        fig,
        [0.13, 0.310, 0.74, 0.060],
        "RPG",
        R["a1"], R["b1"], R["c1"], R["d1"]
    )

    probability_booktabs(
        fig,
        [0.13, 0.205, 0.74, 0.060],
        "Non-RPG",
        R["a0"], R["b0"], R["c0"], R["d0"]
    )

    # --------------------------------------------------------------
    # Within-stratum calculations
    # --------------------------------------------------------------

    fig.text(
        0.13,
        0.137,
        (
            r"$\Delta p_{\mathrm{RPG}}"
            rf"={R['p_r_ads']:.4f}"
            rf"-{R['p_r_noads']:.4f}"
            rf"=\mathbf{{{R['dp_r']:+.4f}}}$"
        ),
        fontsize=8.4,
        color=INK
    )

    fig.text(
        0.53,
        0.137,
        (
            r"$OR_{\mathrm{RPG}}"
            rf"=\frac{{{R['a1']}\times{R['d1']}}}"
            rf"{{{R['b1']}\times{R['c1']}}}"
            rf"=\mathbf{{{R['OR_r']:.4f}}}$"
        ),
        fontsize=8.4,
        color=INK
    )

    fig.text(
        0.13,
        0.093,
        (
            r"$\Delta p_{\mathrm{Non\!-\!RPG}}"
            rf"={R['p_n_ads']:.4f}"
            rf"-{R['p_n_noads']:.4f}"
            rf"=\mathbf{{{R['dp_n']:+.4f}}}$"
        ),
        fontsize=8.4,
        color=INK
    )

    fig.text(
        0.53,
        0.093,
        (
            r"$OR_{\mathrm{Non\!-\!RPG}}"
            rf"=\frac{{{R['a0']}\times{R['d0']}}}"
            rf"{{{R['b0']}\times{R['c0']}}}"
            rf"=\mathbf{{{R['OR_n']:.4f}}}$"
        ),
        fontsize=8.4,
        color=INK
    )

    page_footer(
        fig,
        1
    )

    pdf.savefig(
        fig,
        bbox_inches=None
    )

    plt.close(fig)


# =====================================================================
# PAGE 2
# POOLED INSTALL: INTERACTION
# =====================================================================

def render_page_2(pdf):

    R = install_pooled

    fig = new_page()

    page_header(
        fig,
        "Pooled interaction analysis",
        "Install success  |  Additive and multiplicative scales"
    )

    # =================================================================
    # ADDITIVE
    # =================================================================

    section_heading(
        fig,
        0.855,
        "3",
        "Additive interaction"
    )

    fig.text(
        0.12,
        0.800,
        r"$\mathrm{DDP}"
        r"=\Delta p_{\mathrm{RPG}}"
        r"-\Delta p_{\mathrm{Non\!-\!RPG}}$",
        fontsize=10.5,
        color=TEXT
    )

    fig.text(
        0.12,
        0.757,
        (
            rf"$={R['dp_r']:+.4f}"
            rf"-({R['dp_n']:+.4f})"
            rf"=\mathbf{{{R['DDP']:+.4f}}}$"
        ),
        fontsize=11.0,
        color=INK
    )

    fig.text(
        0.57,
        0.775,
        (
            rf"$95\%\,CI:"
            rf"\ [{R['DDP_low']:.4f},"
            rf"\ {R['DDP_high']:.4f}]$"
        ),
        fontsize=8.5,
        color=TEXT
    )

    ax1 = fig.add_axes(
        [0.10, 0.495, 0.37, 0.205]
    )

    zero_bar_chart(
        ax1,
        [
            "RPG\nΔp",
            "Non-RPG\nΔp",
            "Interaction\nDDP"
        ],
        [
            R["dp_r"],
            R["dp_n"],
            R["DDP"]
        ],
        "Probability difference",
        shades=[
            MID_BAR,
            LIGHT_BAR,
            DARK_BAR
        ]
    )

    ax2 = fig.add_axes(
        [0.56, 0.495, 0.34, 0.205]
    )

    probability_interaction_plot(
        ax2,
        R,
        "Install success"
    )

    caption(
        fig,
        0.455,
        "Figure 1.",
        "Additive interaction. The left panel decomposes the two within-stratum "
        "probability differences and their difference-in-differences; the right "
        "panel shows the corresponding conditional success probabilities."
    )

    # =================================================================
    # MULTIPLICATIVE
    # =================================================================

    section_heading(
        fig,
        0.390,
        "4",
        "Multiplicative interaction"
    )

    fig.text(
        0.12,
        0.337,
        r"$\mathrm{RoR}"
        r"=OR_{\mathrm{RPG}}"
        r"/OR_{\mathrm{Non\!-\!RPG}}$",
        fontsize=10.5,
        color=TEXT
    )

    fig.text(
        0.12,
        0.295,
        (
            rf"$={R['OR_r']:.4f}"
            rf"/{R['OR_n']:.4f}"
            rf"=\mathbf{{{R['RoR']:.4f}}}$"
        ),
        fontsize=11.0,
        color=INK
    )

    fig.text(
        0.57,
        0.313,
        (
            rf"$95\%\,CI:"
            rf"\ [{R['RoR_low']:.4f},"
            rf"\ {R['RoR_high']:.4f}]$"
        ),
        fontsize=8.5,
        color=TEXT
    )

    ax3 = fig.add_axes(
        [0.10, 0.085, 0.37, 0.165]
    )

    zero_bar_chart(
        ax3,
        [
            "RPG\nlog(OR)",
            "Non-RPG\nlog(OR)",
            "Interaction\nlog(RoR)"
        ],
        [
            R["log_OR_r"],
            R["log_OR_n"],
            R["log_RoR"]
        ],
        "Log odds ratio",
        shades=[
            MID_BAR,
            LIGHT_BAR,
            DARK_BAR
        ]
    )

    ax4 = fig.add_axes(
        [0.56, 0.085, 0.34, 0.165]
    )

    log_odds_interaction_plot(
        ax4,
        R,
        "Install success"
    )

    page_footer(
        fig,
        2
    )

    pdf.savefig(fig)
    plt.close(fig)


# =====================================================================
# PAGE 3
# INSTALL CROSS-MARKET
# =====================================================================

def render_page_3(pdf):

    fig = new_page()

    page_header(
        fig,
        "Cross-market replication",
        "Install success  |  United States and India"
    )

    section_heading(
        fig,
        0.855,
        None,
        "Country-specific calculations"
    )

    context_calculation_block(
        fig,
        install_countries["United States"],
        "United States",
        0.805
    )

    context_calculation_block(
        fig,
        install_countries["India"],
        "India",
        0.565
    )

    section_heading(
        fig,
        0.330,
        None,
        "Comparison of interaction estimates"
    )

    context_results_table(
        fig,
        [0.105, 0.230, 0.79, 0.070],
        install_countries
    )

    context_summary_figure(
        fig,
        install_countries,
        [0.10, 0.070, 0.36, 0.120],
        [0.55, 0.070, 0.36, 0.120],
        short_labels=[
            "United States",
            "India"
        ]
    )

    page_footer(
        fig,
        3
    )

    pdf.savefig(fig)
    plt.close(fig)


# =====================================================================
# PAGE 4
# INSTALL TEMPORAL
# =====================================================================

def render_page_4(pdf):

    fig = new_page()

    page_header(
        fig,
        "Temporal replication",
        "Install success  |  Three United States monthly contexts"
    )

    section_heading(
        fig,
        0.855,
        None,
        "Selected monthly contexts"
    )

    y_positions = [
        0.805,
        0.610,
        0.415
    ]

    for (label, R), y in zip(
        install_months.items(),
        y_positions
    ):

        context_calculation_block(
            fig,
            R,
            label,
            y
        )

    section_heading(
        fig,
        0.205,
        None,
        "Temporal comparison"
    )

    context_summary_figure(
        fig,
        install_months,
        [0.10, 0.065, 0.36, 0.105],
        [0.55, 0.065, 0.36, 0.105],
        short_labels=[
            month_label(x)
            for x in INSTALL_MONTHS
        ]
    )

    page_footer(
        fig,
        4
    )

    pdf.savefig(fig)
    plt.close(fig)


# =====================================================================
# PAGE 5
# INSTALL SYNTHESIS
# =====================================================================

def render_page_5(pdf):

    contexts = {
        "Pooled": install_pooled,
        "United States": install_countries["United States"],
        "India": install_countries["India"]
    }

    for label, R in install_months.items():

        contexts[
            f"US {label}"
        ] = R

    fig = new_page()

    page_header(
        fig,
        "Install-success synthesis",
        "Pooled, national, and temporal contexts"
    )

    section_heading(
        fig,
        0.855,
        None,
        "Interaction estimates"
    )

    context_results_table(
        fig,
        [0.085, 0.655, 0.83, 0.145],
        contexts
    )

    section_heading(
        fig,
        0.585,
        None,
        "Interaction magnitude across contexts"
    )

    short_labels = [
        "Pooled",
        "US",
        "India",
        "US\nJan 2025",
        "US\nAug 2025",
        "US\nFeb 2026"
    ]

    context_summary_figure(
        fig,
        contexts,
        [0.095, 0.280, 0.37, 0.245],
        [0.545, 0.280, 0.37, 0.245],
        short_labels=short_labels
    )

    caption(
        fig,
        0.225,
        "Figure 2.",
        "Install-success interaction estimates across the pooled analysis, "
        "two national markets, and three United States monthly contexts. "
        "Both panels use a zero null: DDP on the additive scale and log(RoR) "
        "on the multiplicative scale."
    )

    note(
        fig,
        0.095,
        0.160,
        (
            "The worked contexts are presented to demonstrate how the same "
            "interaction calculation is propagated across analytical levels. "
            "The table retains RoR on its original ratio scale for reporting, "
            "whereas the figure uses log(RoR) so that the multiplicative null "
            "is centered at zero."
        ),
        width=108,
        fontsize=7.4
    )

    page_footer(
        fig,
        5
    )

    pdf.savefig(fig)
    plt.close(fig)


# =====================================================================
# PAGE 6
# RATING POOLED
# =====================================================================

def render_page_6(pdf):

    R = rating_pooled

    fig = new_page()

    page_header(
        fig,
        "Parallel outcome analysis",
        "Outcome 2 — Rating success  |  Pooled analysis"
    )

    section_heading(
        fig,
        0.855,
        "1",
        "Construct the two exposure-by-outcome tables"
    )

    contingency_booktabs(
        fig,
        [0.095, 0.705, 0.37, 0.095],
        "RPG",
        R["a1"], R["b1"], R["c1"], R["d1"]
    )

    contingency_booktabs(
        fig,
        [0.535, 0.705, 0.37, 0.095],
        "Non-RPG",
        R["a0"], R["b0"], R["c0"], R["d0"]
    )

    section_heading(
        fig,
        0.635,
        "2",
        "Estimate within-stratum associations"
    )

    rows = [
        [
            "RPG",
            f"{R['p_r_ads']:.4f}",
            f"{R['p_r_noads']:.4f}",
            f"{R['dp_r']:+.4f}",
            f"{R['OR_r']:.4f}"
        ],
        [
            "Non-RPG",
            f"{R['p_n_ads']:.4f}",
            f"{R['p_n_noads']:.4f}",
            f"{R['dp_n']:+.4f}",
            f"{R['OR_n']:.4f}"
        ]
    ]

    publication_table(
        fig,
        [0.13, 0.535, 0.74, 0.060],
        rows,
        [
            "Stratum",
            "P(success | Ads = 1)",
            "P(success | Ads = 0)",
            "Δp",
            "OR"
        ],
        col_widths=[
            0.18,
            0.25,
            0.25,
            0.16,
            0.16
        ],
        fontsize=7.2,
        row_height=1.45,
        first_col_bold=True
    )

    section_heading(
        fig,
        0.470,
        "3",
        "Estimate interaction on both scales"
    )

    # Additive
    fig.text(
        0.13,
        0.414,
        (
            r"$\mathrm{DDP}"
            rf"={R['dp_r']:+.4f}"
            rf"-({R['dp_n']:+.4f})"
            rf"=\mathbf{{{R['DDP']:+.4f}}}$"
        ),
        fontsize=9.3,
        color=INK
    )

    fig.text(
        0.13,
        0.378,
        (
            rf"$95\%\,CI:"
            rf"\ [{R['DDP_low']:.4f},"
            rf"\ {R['DDP_high']:.4f}]$"
        ),
        fontsize=7.8,
        color=TEXT
    )

    # Multiplicative
    fig.text(
        0.54,
        0.414,
        (
            r"$\mathrm{RoR}"
            rf"={R['OR_r']:.4f}"
            rf"/{R['OR_n']:.4f}"
            rf"=\mathbf{{{R['RoR']:.4f}}}$"
        ),
        fontsize=9.3,
        color=INK
    )

    fig.text(
        0.54,
        0.378,
        (
            rf"$95\%\,CI:"
            rf"\ [{R['RoR_low']:.4f},"
            rf"\ {R['RoR_high']:.4f}]$"
        ),
        fontsize=7.8,
        color=TEXT
    )

    fig.text(
        0.13,
        0.338,
        f"Joint classification:  {R['joint']}",
        fontsize=7.8,
        fontweight="bold",
        color=TEXT
    )

    # --------------------------------------------------------------
    # Compact publication figure
    # --------------------------------------------------------------

    ax1 = fig.add_axes(
        [0.09, 0.095, 0.25, 0.185]
    )

    zero_bar_chart(
        ax1,
        [
            "RPG\nΔp",
            "Non-RPG\nΔp",
            "DDP"
        ],
        [
            R["dp_r"],
            R["dp_n"],
            R["DDP"]
        ],
        "Probability difference",
        shades=[
            MID_BAR,
            LIGHT_BAR,
            DARK_BAR
        ]
    )

    ax2 = fig.add_axes(
        [0.385, 0.095, 0.225, 0.185]
    )

    probability_interaction_plot(
        ax2,
        R,
        "Rating success"
    )

    ax3 = fig.add_axes(
        [0.655, 0.095, 0.25, 0.185]
    )

    zero_bar_chart(
        ax3,
        [
            "RPG\nlog(OR)",
            "Non-RPG\nlog(OR)",
            "log(RoR)"
        ],
        [
            R["log_OR_r"],
            R["log_OR_n"],
            R["log_RoR"]
        ],
        "Log odds ratio",
        shades=[
            MID_BAR,
            LIGHT_BAR,
            DARK_BAR
        ]
    )

    page_footer(
        fig,
        6
    )

    pdf.savefig(fig)
    plt.close(fig)


# =====================================================================
# PAGE 7
# RATING CONTEXTS
# =====================================================================

def render_page_7(pdf):

    fig = new_page()

    page_header(
        fig,
        "Rating-success replication",
        "One national context and one monthly context"
    )

    section_heading(
        fig,
        0.855,
        None,
        "Context-specific calculations"
    )

    context_calculation_block(
        fig,
        rating_us,
        "United States",
        0.805
    )

    context_calculation_block(
        fig,
        rating_month,
        f"United States — {month_label(RATING_MONTH)}",
        0.550
    )

    section_heading(
        fig,
        0.310,
        None,
        "Rating-success summary"
    )

    contexts = {
        "Pooled": rating_pooled,
        "United States": rating_us,
        f"US {month_label(RATING_MONTH)}": rating_month
    }

    context_results_table(
        fig,
        [0.105, 0.210, 0.79, 0.070],
        contexts
    )

    context_summary_figure(
        fig,
        contexts,
        [0.10, 0.065, 0.36, 0.105],
        [0.55, 0.065, 0.36, 0.105],
        short_labels=[
            "Pooled",
            "United States",
            month_label(RATING_MONTH)
        ]
    )

    page_footer(
        fig,
        7
    )

    pdf.savefig(fig)
    plt.close(fig)


# =====================================================================
# PAGE 8
# COMPLETE ANALYSIS SYNTHESIS
#
# This page is intentionally different from the preceding worked pages.
#
# Pages 1–7:
#     demonstrate the calculation using selected contexts.
#
# Page 8:
#     summarizes ALL available national and country × month contexts
#     for BOTH install success and rating success.
# =====================================================================

# =====================================================================
# COMPLETE ADS × RPG SYNTHESIS
# Pages 8–10
#
# Page 8:
#   Complete numerical synthesis across:
#       • pooled analysis
#       • all countries
#       • all country × month contexts
#
# Page 9:
#   Complete country-specific numerical estimates for all national markets.
#
# Page 10:
#   Complete visual synthesis:
#       A. Install DDP — all countries
#       B. Rating DDP  — all countries
#       C. Install DDP — all 14 pooled months
#       D. Rating DDP  — all 14 pooled months
# =====================================================================


# =====================================================================
# 18. COMPLETE CONTEXT CALCULATIONS
# =====================================================================

def calculate_country_results(data, outcome):

    results = {}

    for country in sorted(data["country"].dropna().unique()):

        subset = data[
            data["country"] == country
        ].copy()

        try:
            R = calculate_interaction(
                subset,
                outcome
            )

            if np.isfinite(R["DDP"]) and np.isfinite(R["log_RoR"]):
                results[country] = R

        except Exception:
            continue

    return results


def calculate_country_month_results(data, outcome):

    results = {}

    contexts = (
        data[["country", "month"]]
        .dropna()
        .drop_duplicates()
        .sort_values(["country", "month"])
    )

    for _, row in contexts.iterrows():

        country = row["country"]
        month = row["month"]

        subset = data[
            (data["country"] == country)
            &
            (data["month"] == month)
        ].copy()

        try:
            R = calculate_interaction(
                subset,
                outcome
            )

            if np.isfinite(R["DDP"]) and np.isfinite(R["log_RoR"]):

                results[(country, month)] = R

        except Exception:
            continue

    return results


def calculate_month_results(data, outcome):
    """
    Pooled monthly analysis:
    all countries combined within each month.

    This gives the 14-point temporal series used on Page 9.
    """

    results = {}

    months = (
        data["month"]
        .dropna()
        .sort_values()
        .unique()
        .tolist()
    )

    for month in months:

        subset = data[
            data["month"] == month
        ].copy()

        try:
            R = calculate_interaction(
                subset,
                outcome
            )

            if np.isfinite(R["DDP"]) and np.isfinite(R["log_RoR"]):
                results[month] = R

        except Exception:
            continue

    return results


# =====================================================================
# 19. CALCULATE COMPLETE RESULTS
# =====================================================================

install_country_all = calculate_country_results(
    df,
    INSTALL
)

rating_country_all = calculate_country_results(
    df,
    RATING
)


install_country_month_all = calculate_country_month_results(
    df,
    INSTALL
)

rating_country_month_all = calculate_country_month_results(
    df,
    RATING
)


install_month_all = calculate_month_results(
    df,
    INSTALL
)

rating_month_all = calculate_month_results(
    df,
    RATING
)


# =====================================================================
# 20. SUMMARY HELPERS
# =====================================================================

def summarize_context_results(results):

    values = list(results.values())

    if len(values) == 0:
        return None

    ddp = np.array([
        R["DDP"]
        for R in values
    ])

    ror = np.array([
        R["RoR"]
        for R in values
    ])

    log_ror = np.array([
        R["log_RoR"]
        for R in values
    ])

    counts = {
        "++": 0,
        "--": 0,
        "00": 0,
        "M": 0
    }

    for R in values:

        joint = R["joint"]

        if joint == "++":
            counts["++"] += 1

        elif joint == "--":
            counts["--"] += 1

        elif joint == "00":
            counts["00"] += 1

        else:
            counts["M"] += 1

    return {
        "N": len(values),

        "mean_DDP": np.mean(ddp),
        "median_DDP": np.median(ddp),
        "min_DDP": np.min(ddp),
        "max_DDP": np.max(ddp),

        "mean_RoR": np.mean(ror),
        "median_RoR": np.median(ror),

        "mean_log_RoR": np.mean(log_ror),
        "median_log_RoR": np.median(log_ror),

        "++": counts["++"],
        "--": counts["--"],
        "00": counts["00"],
        "M": counts["M"]
    }


# =====================================================================
# 21. POOLED SUMMARY ROW
# =====================================================================

def pooled_summary_row(
    outcome_name,
    R
):

    return [
        outcome_name,
        "Pooled",

        f"{R['DDP']:+.3f}",

        (
            f"[{R['DDP_low']:+.3f}, "
            f"{R['DDP_high']:+.3f}]"
        ),

        f"{R['RoR']:.3f}",

        f"{R['log_RoR']:+.3f}",

        "1" if R["joint"] == "++" else "0",
        "1" if R["joint"] == "--" else "0",
        "1" if R["joint"] == "00" else "0",
        "1" if R["joint"] not in ["++", "--", "00"] else "0",

        "1"
    ]


# =====================================================================
# 22. AGGREGATED SUMMARY ROW
# =====================================================================

def aggregated_summary_row(
    outcome_name,
    level_name,
    results
):

    S = summarize_context_results(
        results
    )

    return [
        outcome_name,
        level_name,

        f"{S['mean_DDP']:+.3f}",

        (
            f"{S['min_DDP']:+.3f} to "
            f"{S['max_DDP']:+.3f}"
        ),

        f"{S['mean_RoR']:.3f}",

        f"{S['mean_log_RoR']:+.3f}",

        f"{S['++']:,}",
        f"{S['--']:,}",
        f"{S['00']:,}",
        f"{S['M']:,}",

        f"{S['N']:,}"
    ]


# =====================================================================
# PAGE 8
# COMPLETE NUMERICAL SYNTHESIS
# =====================================================================

def render_page_8(pdf):

    fig = new_page()

    page_header(
        fig,
        "Complete Ads × RPG interaction summary",
        "Pooled, cross-market, and temporal evidence"
    )


    # -----------------------------------------------------------------
    # Main synthesis table
    # -----------------------------------------------------------------

    section_heading(
        fig,
        0.855,
        None,
        "Interaction estimates across analytical levels"
    )


    rows = [

        pooled_summary_row(
            "Install",
            install_pooled
        ),

        aggregated_summary_row(
            "Install",
            "Countries",
            install_country_all
        ),

        aggregated_summary_row(
            "Install",
            "Country × month",
            install_country_month_all
        ),

        pooled_summary_row(
            "Rating",
            rating_pooled
        ),

        aggregated_summary_row(
            "Rating",
            "Countries",
            rating_country_all
        ),

        aggregated_summary_row(
            "Rating",
            "Country × month",
            rating_country_month_all
        )
    ]


    publication_table(
        fig,
        [
            0.065,
            0.645,
            0.87,
            0.155
        ],

        rows,

        [
            "Outcome",
            "Analytical\nlevel",
            "Mean /\npooled DDP",
            "95% CI /\nobserved range",
            "Mean /\npooled RoR",
            "Mean /\npooled\nlog(RoR)",
            "++",
            "--",
            "00",
            "Mixed",
            "N"
        ],

        col_widths=[
            0.09,
            0.125,
            0.105,
            0.165,
            0.105,
            0.115,
            0.055,
            0.055,
            0.055,
            0.075,
            0.055
        ],

        fontsize=6.2,
        header_fontsize=5.9,
        row_height=1.55,
        first_col_bold=True
    )


    # -----------------------------------------------------------------
    # Explanation
    # -----------------------------------------------------------------

    fig.text(
        LEFT,
        0.595,
        (
            "Pooled rows report the interaction estimate and its 95% confidence "
            "interval. Country and country × month rows summarize the complete "
            "set of context-specific estimates; the interval column therefore "
            "shows the observed range rather than a confidence interval."
        ),
        fontsize=6.8,
        color=MUTED,
        va="top",
        wrap=True
    )


    # -----------------------------------------------------------------
    # Cross-market detailed table
    # -----------------------------------------------------------------

    section_heading(
        fig,
        0.530,
        None,
        "Cross-market classification"
    )


    install_country_summary = summarize_context_results(
        install_country_all
    )

    rating_country_summary = summarize_context_results(
        rating_country_all
    )


    country_rows = [

        [
            "Install success",

            f"{install_country_summary['mean_DDP']:+.3f}",
            f"{install_country_summary['mean_RoR']:.3f}",

            f"{install_country_summary['++']}",
            f"{install_country_summary['--']}",
            f"{install_country_summary['00']}",
            f"{install_country_summary['M']}",

            f"{install_country_summary['N']}"
        ],

        [
            "Rating success",

            f"{rating_country_summary['mean_DDP']:+.3f}",
            f"{rating_country_summary['mean_RoR']:.3f}",

            f"{rating_country_summary['++']}",
            f"{rating_country_summary['--']}",
            f"{rating_country_summary['00']}",
            f"{rating_country_summary['M']}",

            f"{rating_country_summary['N']}"
        ]
    ]


    publication_table(
        fig,
        [
            0.14,
            0.420,
            0.72,
            0.070
        ],

        country_rows,

        [
            "Outcome",
            "Mean DDP",
            "Mean RoR",
            "++",
            "--",
            "00",
            "Mixed",
            "Countries"
        ],

        col_widths=[
            0.23,
            0.14,
            0.14,
            0.09,
            0.09,
            0.09,
            0.11,
            0.11
        ],

        fontsize=6.8,
        header_fontsize=6.4,
        row_height=1.50,
        first_col_bold=True
    )


    # -----------------------------------------------------------------
    # Country × month detailed table
    # -----------------------------------------------------------------

    section_heading(
        fig,
        0.355,
        None,
        "Country × month classification"
    )


    install_cm_summary = summarize_context_results(
        install_country_month_all
    )

    rating_cm_summary = summarize_context_results(
        rating_country_month_all
    )


    temporal_rows = [

        [
            "Install success",

            f"{install_cm_summary['mean_DDP']:+.3f}",
            f"{install_cm_summary['mean_RoR']:.3f}",

            f"{install_cm_summary['++']}",
            f"{install_cm_summary['--']}",
            f"{install_cm_summary['00']}",
            f"{install_cm_summary['M']}",

            f"{install_cm_summary['N']}"
        ],

        [
            "Rating success",

            f"{rating_cm_summary['mean_DDP']:+.3f}",
            f"{rating_cm_summary['mean_RoR']:.3f}",

            f"{rating_cm_summary['++']}",
            f"{rating_cm_summary['--']}",
            f"{rating_cm_summary['00']}",
            f"{rating_cm_summary['M']}",

            f"{rating_cm_summary['N']}"
        ]
    ]


    publication_table(
        fig,
        [
            0.14,
            0.245,
            0.72,
            0.070
        ],

        temporal_rows,

        [
            "Outcome",
            "Mean DDP",
            "Mean RoR",
            "++",
            "--",
            "00",
            "Mixed",
            "Contexts"
        ],

        col_widths=[
            0.23,
            0.14,
            0.14,
            0.09,
            0.09,
            0.09,
            0.11,
            0.11
        ],

        fontsize=6.8,
        header_fontsize=6.4,
        row_height=1.50,
        first_col_bold=True
    )


    # -----------------------------------------------------------------
    # Definitions
    # -----------------------------------------------------------------

    note(
        fig,
        LEFT,
        0.175,
        (
            "Joint classification combines additive and multiplicative "
            "inference: ++ indicates statistically positive interaction on "
            "both scales; -- indicates statistically negative interaction "
            "on both scales; 00 indicates null interaction on both scales; "
            "Mixed contains all remaining combinations. Multiplicative "
            "effects are reported as RoR in the tables and transformed to "
            "log(RoR) when a zero-centered visual scale is required."
        ),
        width=118,
        fontsize=7.0
    )


    page_footer(
        fig,
        8
    )

    pdf.savefig(fig)

    plt.close(fig)


# =====================================================================
# 23. COUNTRY DDP BAR + CI
# =====================================================================

def country_ddp_panel(
    ax,
    results,
    title
):

    # --------------------------------------------------------------
    # Sort from strongest negative to strongest positive.
    # This reproduces the clear ordered appearance of your existing
    # national-market figure.
    # --------------------------------------------------------------

    items = sorted(
        results.items(),
        key=lambda item: item[1]["DDP"]
    )

    labels = [
        str(k)
        for k, _ in items
    ]

    values = np.array([
        R["DDP"]
        for _, R in items
    ])

    lows = np.array([
        R["DDP_low"]
        for _, R in items
    ])

    highs = np.array([
        R["DDP_high"]
        for _, R in items
    ])


    x = np.arange(
        len(values)
    )


    lower_error = values - lows
    upper_error = highs - values


    ax.bar(
        x,
        values,
        width=0.72,
        color="0.56",
        edgecolor="0.28",
        linewidth=0.30,
        zorder=2
    )


    ax.errorbar(
        x,
        values,
        yerr=[
            lower_error,
            upper_error
        ],
        fmt="none",
        ecolor="0.28",
        elinewidth=0.45,
        capsize=1.2,
        capthick=0.45,
        zorder=3
    )


    ax.axhline(
        0,
        color=INK,
        linewidth=0.70,
        linestyle="--",
        zorder=4
    )


    ax.set_xticks(
        x
    )


    ax.set_xticklabels(
        labels,
        rotation=90,
        fontsize=4.6
    )


    ax.set_ylabel(
        "DDP",
        fontsize=6.8
    )


    ax.set_title(
        title,
        fontsize=8.3,
        fontweight="bold",
        loc="left",
        pad=7
    )


    ax.text(
        0.002,
        0.975,
        "Null: DDP = 0",
        transform=ax.transAxes,
        fontsize=5.5,
        color=MUTED,
        va="top"
    )


    clean_axis(
        ax
    )


# =====================================================================
# 24. MONTHLY DDP PANEL
# =====================================================================

def monthly_ddp_panel(
    ax,
    results,
    title
):

    items = sorted(
        results.items(),
        key=lambda item: item[0]
    )


    labels = [
        month_label(k)
        for k, _ in items
    ]


    values = np.array([
        R["DDP"]
        for _, R in items
    ])


    lows = np.array([
        R["DDP_low"]
        for _, R in items
    ])


    highs = np.array([
        R["DDP_high"]
        for _, R in items
    ])


    x = np.arange(
        len(values)
    )


    lower_error = values - lows
    upper_error = highs - values


    ax.errorbar(
        x,
        values,
        yerr=[
            lower_error,
            upper_error
        ],
        fmt="o-",
        color="0.22",
        ecolor="0.48",
        linewidth=0.85,
        elinewidth=0.55,
        markersize=2.8,
        capsize=1.5,
        zorder=3
    )


    ax.axhline(
        0,
        color=INK,
        linewidth=0.70,
        linestyle="--"
    )


    ax.set_xticks(
        x
    )


    # Jan\n2025 style, as in your current figure
    compact_labels = []

    for label in labels:

        parts = label.split()

        if len(parts) >= 2:

            compact_labels.append(
                parts[0] + "\n" + parts[-1]
            )

        else:

            compact_labels.append(
                label
            )


    ax.set_xticklabels(
        compact_labels,
        fontsize=4.8
    )


    ax.set_ylabel(
        "DDP",
        fontsize=6.8
    )


    ax.set_xlabel(
        "Month",
        fontsize=6.4
    )


    ax.set_title(
        title,
        fontsize=8.3,
        fontweight="bold",
        loc="left",
        pad=7
    )


    ax.text(
        0.002,
        0.975,
        "Null: DDP = 0",
        transform=ax.transAxes,
        fontsize=5.5,
        color=MUTED,
        va="top"
    )


    clean_axis(
        ax
    )


# =====================================================================
# PAGE 9
# COMPLETE COUNTRY-SPECIFIC NUMERICAL RESULTS
# =====================================================================

def render_page_9(pdf):

    fig = new_page()

    page_header(
        fig,
        "Country-specific interaction estimates",
        "Ads × RPG interaction  |  All national markets"
    )

    section_heading(
        fig,
        0.855,
        None,
        "Install and rating interaction estimates by country"
    )

    # -----------------------------------------------------------------
    # One row per national market.
    # The complete country-level results have already been calculated
    # above as install_country_all and rating_country_all.
    # -----------------------------------------------------------------

    countries = sorted(
        set(install_country_all.keys())
        | set(rating_country_all.keys())
    )

    rows = []

    for country in countries:

        I = install_country_all.get(country)
        R = rating_country_all.get(country)

        if I is not None:
            install_ddp = (
                f"{I['DDP']:+.3f} "
                f"[{I['DDP_low']:+.3f}, {I['DDP_high']:+.3f}]"
            )
            install_ror = (
                f"{I['RoR']:.3f} "
                f"[{I['RoR_low']:.3f}, {I['RoR_high']:.3f}]"
            )
        else:
            install_ddp = "—"
            install_ror = "—"

        if R is not None:
            rating_ddp = (
                f"{R['DDP']:+.3f} "
                f"[{R['DDP_low']:+.3f}, {R['DDP_high']:+.3f}]"
            )
            rating_ror = (
                f"{R['RoR']:.3f} "
                f"[{R['RoR_low']:.3f}, {R['RoR_high']:.3f}]"
            )
        else:
            rating_ddp = "—"
            rating_ror = "—"

        rows.append([
            str(country),
            install_ddp,
            install_ror,
            rating_ddp,
            rating_ror
        ])

    # -----------------------------------------------------------------
    # Dense but readable A4 table: all 42 countries on one page.
    # -----------------------------------------------------------------

    publication_table(
        fig,
        [
            0.055,
            0.095,
            0.89,
            0.700
        ],
        rows,
        [
            "Country",
            "Install DDP [95% CI]",
            "Install RoR [95% CI]",
            "Rating DDP [95% CI]",
            "Rating RoR [95% CI]"
        ],
        col_widths=[
            0.12,
            0.22,
            0.22,
            0.22,
            0.22
        ],
        fontsize=4.85,
        header_fontsize=5.15,
        row_height=0.92,
        first_col_bold=True,
        alignments=[
            "left",
            "center",
            "center",
            "center",
            "center"
        ]
    )

    fig.text(
        LEFT,
        0.070,
        (
            "Each row reports the country-specific Ads × RPG interaction estimate "
            "and its 95% confidence interval. DDP is the additive interaction "
            "(null = 0); RoR is the multiplicative interaction (null = 1). "
            "The table reports the complete national-market estimates rather than "
            "cross-country means."
        ),
        fontsize=6.2,
        color=MUTED,
        va="top",
        wrap=True
    )

    page_footer(
        fig,
        9
    )

    pdf.savefig(fig)
    plt.close(fig)


# =====================================================================
# PAGE 10
# COMPLETE VISUAL SYNTHESIS
# =====================================================================

def render_page_10(pdf):

    fig = new_page()


    page_header(
        fig,
        "Complete cross-market and temporal synthesis",
        "Ads × RPG interaction  |  Install success and rating success"
    )


    # =================================================================
    # COUNTRY RESULTS
    # =================================================================

    section_heading(
        fig,
        0.855,
        None,
        "Cross-market interaction — all national markets"
    )


    ax1 = fig.add_axes(
        [
            0.09,
            0.600,
            0.39,
            0.195
        ]
    )


    country_ddp_panel(
        ax1,
        install_country_all,
        "A   Install success"
    )


    ax2 = fig.add_axes(
        [
            0.55,
            0.600,
            0.39,
            0.195
        ]
    )


    country_ddp_panel(
        ax2,
        rating_country_all,
        "B   Rating success"
    )


    fig.text(
        LEFT,
        0.565,
        (
            "Countries are ordered independently by estimated DDP within "
            "each outcome. Bars show the interaction estimate; whiskers show "
            "95% confidence intervals."
        ),
        fontsize=6.4,
        color=MUTED
    )


    # =================================================================
    # MONTH RESULTS
    # =================================================================

    section_heading(
        fig,
        0.515,
        None,
        "Temporal interaction — all 14 pooled months"
    )


    ax3 = fig.add_axes(
        [
            0.09,
            0.285,
            0.39,
            0.175
        ]
    )


    monthly_ddp_panel(
        ax3,
        install_month_all,
        "C   Install success"
    )


    ax4 = fig.add_axes(
        [
            0.55,
            0.285,
            0.39,
            0.175
        ]
    )


    monthly_ddp_panel(
        ax4,
        rating_month_all,
        "D   Rating success"
    )


    fig.text(
        LEFT,
        0.245,
        (
            "Monthly estimates pool all national markets within each calendar "
            "month. Points show monthly DDP estimates and whiskers show 95% "
            "confidence intervals. Month order is preserved because the "
            "horizontal axis represents time."
        ),
        fontsize=6.4,
        color=MUTED,
        wrap=True
    )


    # =================================================================
    # SHORT READER GUIDE
    # =================================================================

    add_line(
        fig,
        LEFT,
        RIGHT,
        0.195,
        color=LIGHT_RULE,
        lw=0.45
    )


    fig.text(
        LEFT,
        0.168,
        "Reading the figure",
        fontsize=7.4,
        fontweight="bold",
        color=INK
    )


    note(
        fig,
        LEFT,
        0.145,
        (
            "DDP = 0 is the additive no-interaction reference. Values below "
            "zero indicate that the Ads-associated probability difference is "
            "more negative for RPG than for non-RPG games; values above zero "
            "indicate the reverse. The corresponding multiplicative evidence "
            "is retained in the complete numerical synthesis on the preceding "
            "page using RoR and log(RoR)."
        ),
        width=116,
        fontsize=6.8
    )


    page_footer(
        fig,
        10
    )


    pdf.savefig(fig)

    plt.close(fig)
# =====================================================================
# 19. GENERATE PDF
# =====================================================================

with PdfPages(OUTPUT_FILE) as pdf:

    render_page_1(pdf)
    render_page_2(pdf)
    render_page_3(pdf)
    render_page_4(pdf)
    render_page_5(pdf)
    render_page_6(pdf)
    render_page_7(pdf)

    # Complete synthesis
    render_page_8(pdf)
    render_page_9(pdf)
    render_page_10(pdf)


# =====================================================================
# 20. CONSOLE SUMMARY
# =====================================================================

print()
print("=" * 78)
print("PUBLICATION-STYLE WORKED EXAMPLE CREATED")
print("=" * 78)

print()
print(f"Output: {OUTPUT_FILE}")

print()
print("Structure:")
print("  Page 1  Install — pooled data construction")
print("  Page 2  Install — pooled DDP and RoR interaction")
print("  Page 3  Install — United States and India")
print("  Page 4  Install — three United States months")
print("  Page 5  Install — synthesis")
print("  Page 6  Rating — pooled worked analysis")
print("  Page 7  Rating — United States + one monthly example")
print("  Page 8  Install + rating synthesis")
print("  Page 9  All 42 country-specific numerical estimates")
print("  Page 10 Complete visual synthesis")

print()
print("Install temporal contexts:")

for m in INSTALL_MONTHS:
    print(f"  • {month_label(m)}")

print()
print(
    "Rating temporal context:"
    f" {month_label(RATING_MONTH)}"
)

print()
print("Visual multiplicative scale:")
print("  log(RoR), with null = 0")

print()
print("Reported multiplicative scale:")
print("  RoR with 95% CI")

print()
print("=" * 78)