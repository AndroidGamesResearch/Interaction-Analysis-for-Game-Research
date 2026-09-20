# Interaction Analysis for Game Research

This repository provides the supplementary materials, analysis code, and research artifacts associated with a study introducing an **Interaction-Analysis Framework** for examining contextual variation in empirical relationships in game research.

The framework provides a systematic and reproducible approach for identifying, estimating, evaluating, and interpreting whether empirical relationships vary across different contexts.

## Interaction-Analysis Framework

The framework consists of seven stages:

1. Constructing contingency tables
2. Estimating conditional success probabilities
3. Assessing differences in proportions
4. Estimating conditional odds ratios
5. Evaluating additive interaction
6. Evaluating multiplicative interaction
7. Interpreting interaction effects

Interaction is evaluated on both **additive and multiplicative scales**, together with the corresponding stratum-specific relationships and 95% confidence intervals.

## Empirical Application

The framework is demonstrated through an analysis of monetization–marketplace-success relationships in free-to-play Android mobile games.

The empirical analysis examines contextual variation across:

- Game genres
- National markets
- Time
- Gameplay characteristics
- National demographic, economic, developmental, and digital conditions

The analysis uses **1,778,700 game–market–month observations**, covering **10 game genres, 42 national markets, and 14 monthly periods**.

## Repository Contents

The repository will contain:

- Implementation of the Interaction-Analysis Framework
- Experimental analysis scripts
- Supplementary experimental results
- Game-level gameplay characterizations
- Gameplay coding matrices
- Profile-level calculations
- Cross-market and temporal analysis outputs
- National-context analysis outputs
- Figures and supporting materials

## Repository Structure

```text
.
├── src/                 # Interaction-analysis implementation
├── experiments/         # Empirical analysis scripts
├── supplementary/       # Supplementary tables and research artifacts
├── results/             # Experimental outputs
├── figures/             # Supporting figures
├── requirements.txt     # Python dependencies
└── README.md
