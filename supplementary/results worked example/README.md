# Worked Interaction-Analysis Examples

This directory contains the complete worked examples accompanying the
Interaction-Analysis Framework presented in the paper. These materials
document the analytical procedure used to obtain the worked-example results
and provide the corresponding publication-style outputs for inspection and
verification.

Three monetization–genre interactions are included:

- **Ads × RPG** — illustrates a negative interaction profile.
- **IAP × RPG** — illustrates a positive interaction profile recurring across
  the examined national and temporal contexts.
- **IAP × Sports** — illustrates a context-varying interaction profile, with
  interaction direction and statistical support varying across national
  markets.

Together, these examples demonstrate the application of the same interaction-
analysis procedure to negative, positive, and context-varying empirical
relationships.

## Files

Each worked example is provided as a Python analysis script and its
corresponding generated PDF.

| Worked example | Analysis script | Worked-example output |
|---|---|---|
| Ads × RPG | `ads_rpg_worked_example.py` | `ads_rpg_worked_example.pdf` |
| IAP × RPG | `iap_rpg_worked_example.py` | `iap_rpg_worked_example.pdf` |
| IAP × Sports | `iap_sports_worked_example.py` | `iap_sports_worked_example.pdf` |

The Python scripts contain the complete analytical procedure used for each
example, including construction of the comparison groups, conditional success
probabilities, additive and multiplicative interaction estimates, 95%
confidence intervals, and analyses across national and temporal contexts.

The corresponding PDFs present the complete worked analyses in a
reader-oriented format, including the intermediate calculations, estimates,
tables, and visual summaries used to illustrate the framework in the paper.

## Purpose

These worked examples are provided as supplementary methodological material
to make the implementation of the Interaction-Analysis Framework transparent
and to document how the reported interaction results are derived.

The broader study analysis pipeline and study-level outputs are available
separately in the repository's `code/` and `results/` directories.
