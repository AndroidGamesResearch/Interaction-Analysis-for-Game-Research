
# Stage 5 — National-Context Analysis

This folder contains the supplementary data materials supporting **Stage 5 — National-Context Analysis**.

## Purpose

This stage examines whether cross-country variation in the magnitude of recurring monetization × genre interactions is associated with national contextual characteristics.

The analysis focuses on five recurring positive interaction profiles:

### Ads
- Ads × Casual
- Ads × Puzzle

### In-App Purchases (IAP)
- IAP × RPG
- IAP × Strategy
- IAP × Simulation

For each profile, country-specific additive interaction estimates (DDP) are related to national contextual indicators across the 42 markets included in the study.

---

## National Context Indicators

Five national indicators are examined:

1. **Median age**
2. **PPP-adjusted GDP per capita**
3. **Human Development Index (HDI)**
4. **Internet penetration**
5. **Digital-payment adoption**

The indicators were obtained from the original external data sources reported in the manuscript.

The source datasets were downloaded in their original formats and used to construct the consolidated country-level dataset included in this folder.

---

## Source Data

The national-context dataset was assembled from the original demographic, economic, human-development, internet-use, and digital-payment data sources.

The source materials include data corresponding to:

- population median age;
- GDP per capita adjusted for purchasing power parity (PPP);
- Human Development Index (HDI);
- individuals using the Internet; and
- digital-payment adoption.

The original source files retain the filenames and formats supplied by their respective data providers.

Some original source datasets are large and are therefore not redistributed in this repository. Their original sources are identified in the manuscript so that the underlying data can be retrieved directly from the corresponding providers.

The processed 42-country dataset used in the empirical analysis is provided here to document the values entering Stage 5.

---

## Construction of the 42-Country Dataset

The national indicators from the separate source datasets were matched to the **42 national Google Play markets** examined in the study.

The resulting consolidated dataset is:

`country_context_indicators_42.csv`

This file contains the country-level contextual indicators used in the Stage 5 analysis after extraction and alignment of the relevant values from the original source datasets.

It therefore provides the analysis-ready national-context data used to associate country characteristics with variation in interaction magnitude.

---

## Country-Specific Interaction Estimates

For each of the five retained interaction profiles, the analysis uses the country-specific additive interaction estimate (**DDP**) for install success.

These estimates represent the magnitude of the corresponding monetization × genre interaction within each national market.

The country-specific interaction data used for the Stage 5 analysis are provided in:

`figure_country_ddp_42countries.xls`

This file contains the country-level DDP information for the 42 markets used in the cross-country characterization and associated figure preparation.

---

## Statistical Analysis

For each of the five interaction profiles, country-specific DDP estimates are matched to each of the five national contextual indicators.

Associations are evaluated using **Spearman rank correlation**.

This produces:

**5 interaction profiles × 5 national indicators = 25 profile–indicator associations**

The 25 resulting p-values are adjusted jointly using the **Benjamini–Hochberg false discovery rate (FDR)** procedure.

Statistical significance is evaluated using:

**p_FDR < 0.05**

The Spearman correlation and FDR-adjustment code is contained in the repository's complete empirical analysis script and is therefore not duplicated in this supplementary folder.

---

## Files in This Folder

### `country_context_indicators_42.csv`

Consolidated analysis-ready national-context dataset for the 42 markets.

It combines the national indicators extracted and aligned from the original external data sources and provides the contextual variables used in the Stage 5 correlation analysis.

### `figure_country_ddp_42countries.xls`

Country-specific DDP data for the five recurring positive monetization × genre interaction profiles across the 42 national markets.

This file supports the cross-country characterization analysis and associated figure preparation.

### Original Source Data

The national indicators were derived from the original datasets identified in the manuscript.

Where practical, original downloaded source files may also be retained with the supplementary research materials. Large original datasets are not necessarily redistributed through this repository; the manuscript provides their corresponding data sources, while `country_context_indicators_42.csv` provides the processed values actually used in the analysis.
