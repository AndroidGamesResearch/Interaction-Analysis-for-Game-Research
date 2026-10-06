# Supplementary Table S1. Empirical Components of the Analysis

This table provides the complete operational specification of the empirical design.

| Component | Operationalisation |
|---|---|
| **Platform** | Google Play Store |
| **Study population** | Free-to-play (F2P) Android mobile games |
| **Observations** | 1,778,700 game–market–month observations |
| **Monetization (`r`)** | Ads and in-app purchases (IAP), analysed separately as binary indicators of presence |
| **Game context (`c_j`)** | 10 genres: Puzzle (`n = 847`), Action (`n = 488`), Simulation (`n = 316`), Sports (`n = 232`), RPG (`n = 227`), Educational (`n = 212`), Casual (`n = 205`), Arcade (`n = 188`), Strategy (`n = 179`), and Racing (`n = 131`). Each genre is compared with all remaining genres (`c_j` vs. `\bar{c}_j`). |
| **Install success (`y_install`)** | Installs at or above the country–month median |
| **Rating success (`y_rating`)** | Rating at or above the country–month median |
| **National market (`C`)** | 42 national markets: Vietnam, Pakistan, Indonesia, India, Peru, South Africa, Philippines, Thailand, Russia, Mexico, Malaysia, Brazil, Chile, Netherlands, Belgium, Argentina, Portugal, Spain, Colombia, Taiwan, Japan, Sweden, Italy, Ireland, France, Switzerland, South Korea, United Arab Emirates, Austria, United States, Finland, Germany, Australia, Denmark, New Zealand, Poland, Canada, Saudi Arabia, Norway, United Kingdom, Hong Kong, and Singapore |
| **Temporal context (`T`)** | 14 monthly periods, January 2025–February 2026, examined separately within each national market |
| **Gameplay characteristics** | 8 game-level characteristics used to characterise the forms of play associated with recurring monetization–genre interaction profiles |
| **National indicators** | Median age, PPP-adjusted GDP per capita, Human Development Index (HDI), Internet penetration, and digital-payment adoption |
| **Interaction estimation** | Additive interaction estimated using the difference of differences in success probabilities (DDP); multiplicative interaction estimated using the ratio of conditional odds ratios (RoR) |
| **Statistical uncertainty** | 95% confidence intervals; game-level cluster bootstrap where repeated observations of the same game require dependence to be accounted for |
| **National-context analysis** | Spearman's rank correlation between country-specific additive interaction estimates (DDP) and national indicators, with Benjamini–Hochberg false discovery rate (FDR) correction |
