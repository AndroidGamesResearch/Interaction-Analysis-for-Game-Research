# Worked Interaction-Analysis Examples

This directory provides the complete worked examples accompanying the
Interaction-Analysis Framework presented in the paper. The materials are
included to make the analytical procedure transparent and to allow readers
to inspect and verify the calculations and results illustrated in the study.

Three monetization–genre interactions are provided:

- **Ads × RPG** — demonstrates a negative interaction profile.
- **IAP × RPG** — demonstrates a positive interaction profile that recurs
  across the examined national and temporal contexts.
- **IAP × Sports** — demonstrates a context-dependent profile in which
  interaction direction and statistical support vary across national markets.

Together, the examples illustrate how the same analytical framework is used
to identify negative, positive, and context-varying interaction profiles.

## Files

Each worked example is provided in two formats:

| Worked example | Reproducible analysis | Generated output |
|---|---|---|
| Ads × RPG | `ads_rpg_worked_example.py` | `ads_rpg_worked_example.pdf` |
| IAP × RPG | `iap_rpg_worked_example.py` | `iap_rpg_worked_example.pdf` |
| IAP × Sports | `iap_sports_worked_example.py` | `iap_sports_worked_example.pdf` |

The **Python scripts** reproduce the complete analytical workflow for each
example, including data construction, conditional success probabilities,
additive and multiplicative interaction estimates, 95% confidence intervals,
and country- and time-specific analyses.

The corresponding **PDF files** are the generated publication-style worked
examples, allowing the analytical steps and resulting estimates to be
inspected without executing the code.

## Reproducing the Worked Examples

The scripts assume that the study dataset has already been loaded as the
pandas DataFrame `apps`. Each script can then be executed to generate its
corresponding PDF:

```python
exec(open("ads_rpg_worked_example.py").read())
