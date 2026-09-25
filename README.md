# Interaction Analysis for Game Research

This repository provides the analysis code, empirical outputs, figures, and supplementary materials associated with a study introducing an **Interaction-Analysis Framework for Game Research**.

The framework provides a systematic and reproducible approach for examining the **contextual scope of empirical relationships**: whether a relationship observed overall remains equivalent, weakens, disappears, or changes direction across the contexts represented in the evidence.

The empirical application examines relationships between mobile-game monetization mechanisms — **advertising (Ads)** and **in-app purchases (IAP)** — and marketplace success across gameplay, national, and temporal contexts.

---

## Study Visual Summary

A one-page visual map provides an overview of the complete study, connecting the research problem and methodological motivation to the study design, five analytical stages, principal empirical findings, contributions, and implications.

**[View the One-Page Visual Map of the Entire Study](study%20visual%20summary/one_page_visual_map_of_the_entire_study.pdf)**

---

## Interaction-Analysis Framework

The framework adapts principles of **interaction and effect-measure modification** to game research. Rather than asking only whether a feature is associated with an outcome, it examines whether that relationship itself differs across relevant contexts.

The analytical procedure consists of seven steps:

1. Construct contingency tables
2. Estimate conditional success probabilities
3. Estimate probability differences
4. Estimate conditional odds ratios
5. Estimate additive interaction
6. Estimate multiplicative interaction
7. Interpret the interaction evidence

Interaction is evaluated on two complementary scales:

- **Additive interaction — Difference in Differences of Probabilities (DDP)**
- **Multiplicative interaction — Ratio of Odds Ratios (RoR)**

Both measures are evaluated with **95% confidence intervals**, alongside the corresponding stratum-specific relationships.

---

## Empirical Application

The framework is demonstrated through an analysis of monetization–marketplace-success relationships in free-to-play Android mobile games.

The study comprises **1,778,700 game–market–month observations** spanning:

- **10 game genres**
- **42 national markets**
- **14 monthly periods**
- **Ads and IAP**, analysed separately
- **Install success and rating success**

The empirical analysis proceeds through five stages.

### Stage 1 — Genre Conditioning

Examines whether the overall monetization–success relationship changes when conditioned on game genre.

### Stage 2 — Cross-Market Recurrence

Re-applies the framework within individual national markets to determine whether conditional relationships recur across countries.

### Stage 3 — Temporal Stability

Re-applies the framework within country–month contexts to examine whether recurring relationships persist as the marketplace evolves.

### Stage 4 — Forms of Play

Characterizes games belonging to recurring interaction profiles to examine the gameplay structures represented by positive and negative monetization–success relationships.

### Stage 5 — National Conditions

Examines whether variation in interaction magnitude across national markets is associated with demographic, economic, developmental, and digital conditions.

All estimates represent **associations within observational marketplace data**; no causal effects are claimed.

---

## Repository Structure

```text
.
├── code/                    # Framework implementation and main analysis code
├── data/                    # Data documentation and related materials
├── figures/                 # Figures used in the associated paper
├── results/                 # Main empirical analysis outputs
├── study visual summary/    # One-page visual map of the entire study
├── supplementary/           # Detailed supporting and verification materials
├── .gitignore
└── README.md
```

---

## Code

The `code/` directory contains the implementation of the Interaction-Analysis Framework and the main analysis workflow used in the study.

It includes code supporting:

- genre-level interaction analysis
- cross-market interaction analysis
- temporal interaction analysis
- gameplay characterization
- national-context analysis

The implementation estimates stratum-specific success probabilities and odds ratios together with additive and multiplicative interaction and their corresponding statistical uncertainty.

---

## Figures

The `figures/` directory contains the principal figures used in the associated paper.

These include visualizations of:

- Ads × RPG interaction profiles
- IAP × RPG interaction profiles
- IAP × Sports interaction profiles
- within-RPG monetization comparisons
- gameplay characterization
- national-context relationships
- the Cultural Paradox of Success
- the overall analytical setup

These figures correspond to the principal methodological, empirical, and conceptual results presented in the manuscript.

---

## Results

The `results/` directory contains the principal outputs generated across the empirical analysis.

These include:

- dataset overview
- Stage 1 genre-level pooled output
- Stage 2 cross-market output
- Stage 3 temporal output
- Stage 5 national-context output
- consolidated analytical summary

These materials provide study-level outputs from the main analytical pipeline.

---

## Study Visual Summary

The `study visual summary/` directory contains the **One-Page Visual Map of the Entire Study**.

The visual integrates the:

- research problem
- methodological gap
- Interaction-Analysis Framework
- research objective and question
- data and study design
- five analytical stages
- principal empirical findings
- Cultural Paradox of Success
- methodological, empirical, and conceptual contributions
- research and practical implications

It is intended as a compact guide to the overall logic of the study and to how its methodological, empirical, and conceptual components connect.

**[Open the One-Page Visual Map of the Entire Study](study%20visual%20summary/one_page_visual_map_of_the_entire_study.pdf)**

---

## Supplementary Materials

The `supplementary/` directory contains detailed materials supporting the analyses reported in the study.

### Gameplay Characterisation

Supporting materials for the gameplay-characterization stage include:

- selected-game lists
- game-selection outputs
- game-level characterization materials
- gameplay coding resources
- profile-level materials
- methodological documentation
- conceptual gameplay visualization

### Markets Characterisation

Supporting materials for the national-context stage include:

- country-context indicators
- country-level interaction information
- supporting national-context figures and materials

### Worked Interaction-Analysis Examples

Three complete worked examples are provided to make the implementation of the framework transparent and to show how selected interaction results are derived.

| Worked example | Profile illustrated | Materials |
|---|---|---|
| **Ads × RPG** | Recurring negative interaction | Python script + complete PDF |
| **IAP × RPG** | Recurring positive interaction | Python script + complete PDF |
| **IAP × Sports** | Context-varying interaction | Python script + complete PDF |

Each worked example documents the analytical process from contingency-table construction and conditional probabilities through DDP and RoR estimation, 95% confidence intervals, and country- and time-specific evaluation.

**[View the worked interaction-analysis examples](supplementary/results%20worked%20example/)**

---

## Data

The empirical application uses a cross-country panel of Android mobile-game marketplace observations covering national Google Play markets and monthly observation periods.

The underlying research dataset is **not distributed through this repository at present**.

The repository therefore focuses on documenting the analytical framework, implementation, study outputs, figures, and supplementary methodological materials.

---

## Reproducibility and Transparency

The repository is organized to make the analytical path from framework implementation to reported evidence transparent.

- `code/` documents the implementation and main analytical workflow.
- `results/` provides the corresponding stage-level empirical outputs.
- `figures/` contains the figures used in the associated paper.
- `supplementary/` provides detailed supporting analyses and worked examples.
- `study visual summary/` provides a consolidated map of the complete study.

The worked interaction-analysis examples additionally expose the intermediate calculations underlying selected empirical profiles, including contingency tables, conditional probabilities, additive and multiplicative interaction estimates, confidence intervals, and contextual replication.

Together, these materials document how the reported evidence was constructed and how the Interaction-Analysis Framework was applied across gameplay, national, and temporal contexts.

---

## Citation

This repository accompanies the research study introducing the **Interaction-Analysis Framework for Game Research**.

The associated manuscript is currently under publication consideration. A complete bibliographic citation and DOI will be added here upon publication.

If you use or refer to materials from this repository before publication, please cite the repository directly.
