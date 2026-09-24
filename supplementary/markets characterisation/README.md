# Stage 5 — National-Context Analysis

This folder contains the supplementary data used for the national-context analysis.

Five country-level indicators were used to characterize the 42 national markets:

- **Median age (Age)** — demographic structure.  
  Source: United Nations, *World Population Prospects 2024*.

- **GDP per capita, PPP (PPP)** — purchasing capacity.  
  Source: World Bank, *GDP per capita, PPP (current international $)* (`NY.GDP.PCAP.PP.CD`).

- **Human Development Index (HDI)** — socioeconomic development.  
  Source: United Nations Development Programme (UNDP), *Human Development Report 2025*.

- **Internet penetration (NET)** — digital access.  
  Source: World Bank, *Individuals using the Internet (% of population)* (`IT.NET.USER.ZS`).

- **Digital-payment adoption (DP)** — participation in digital transactions.  
  Source: World Bank, *Global Findex Database 2025*.

## Source Links

- World Population Prospects: https://population.un.org/wpp/
- World Bank — GDP per capita, PPP: https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.CD
- UNDP — Human Development Report: https://hdr.undp.org/
- World Bank — Individuals using the Internet: https://data.worldbank.org/indicator/IT.NET.USER.ZS
- World Bank — Global Findex Database: https://www.worldbank.org/en/publication/globalfindex

The original source datasets were downloaded from these providers. Some of the original files are large and are therefore not duplicated in this repository; the original sources are provided above and in the manuscript.

## Files

### `country_context_indicators_42.csv`

Contains the five national-context indicators extracted from the original sources and matched to the 42 national markets included in the study.

### `figure_country_ddp_42countries.xls`

Contains the country-level data brought together for the Stage 5 analysis, including the country-specific interaction estimates used alongside the national-context indicators.

The Spearman correlation analysis and Benjamini–Hochberg FDR correction are implemented in the complete analysis script provided in the main repository.
