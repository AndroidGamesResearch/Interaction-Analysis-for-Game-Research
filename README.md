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

The repository contains:

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
├── data/                 # Data information and analysis inputs
├── code/                 # Framework implementation and analysis scripts
├── supplementary/        # Detailed supplementary research materials
├── figures/              # Supporting figures and visualizations
├── requirements.txt      # Python dependencies
└── README.md
```

## Data

The empirical analysis uses a cross-country dataset of Android mobile games covering multiple national Google Play markets and monthly observation periods.

Information required to access the underlying dataset is provided with the research materials.

## Code

The repository provides the analysis code used to implement the Interaction-Analysis Framework and reproduce the empirical analyses reported in the associated study.

The code covers the main stages of the empirical analysis:

- Genre-level interaction analysis
- Cross-market interaction analysis
- Temporal interaction analysis
- Gameplay characterization analysis
- National-context analysis

The implementation includes estimation of stratum-specific relationships and interaction on both additive and multiplicative scales, together with the corresponding statistical uncertainty measures.

Code and analysis scripts are provided in the `code/` directory.

## Reproducibility

The repository is organized to support reproduction of the analyses reported in the associated study.

Scripts, dependencies, analysis inputs, experimental outputs, and supplementary materials are provided in their corresponding directories. Instructions for executing the analyses and reproducing the reported results are provided with the relevant code.

## Supplementary Materials

Detailed supplementary materials include:

- Complete game-level gameplay characterizations
- Gameplay-characteristic coding matrices
- Profile-level calculations
- Country-level interaction estimates
- Temporal interaction estimates
- National-context analysis results

The supplementary materials are provided in the `supplementary/` directory.

## Citation

Citation information will be added following publication of the associated research.
