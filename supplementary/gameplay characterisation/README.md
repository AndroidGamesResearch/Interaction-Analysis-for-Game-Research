
# Stage 4 — Gameplay Characterization

This folder contains the materials supporting **Stage 4 — Gameplay Characterization** of the empirical analysis.

## Purpose

Stages 1–3 identify monetization × genre interaction profiles and examine their recurrence across pooled, national-market, and temporal contexts.

Stage 4 moves from these statistical interaction profiles to the **game level**. Its purpose is to characterize the forms of gameplay associated with recurring positive and negative Ads and in-app purchase (IAP) interaction profiles.

The analysis asks whether interaction profiles with different directions are also associated with systematically different gameplay characteristics.

---

## Interaction Profiles Examined

Nine recurring monetization × genre profiles were selected for gameplay characterization.

### Ads

**Positive interaction profiles**
- Ads × Casual
- Ads × Puzzle

**Negative interaction profiles**
- Ads × Strategy
- Ads × RPG

### In-App Purchases (IAP)

**Positive interaction profiles**
- IAP × RPG
- IAP × Strategy
- IAP × Simulation

**Negative interaction profiles**
- IAP × Casual
- IAP × Puzzle

These profiles provide the basis for comparing gameplay characteristics associated with positive and negative interaction directions within each monetization mechanism.

---

## Game Selection

Games were selected separately for each of the nine interaction profiles.

For each profile:

1. Games belonging to the corresponding genre and monetization condition were identified.
2. Install-success performance was calculated for each eligible game.
3. Games were ranked by **install-success rate**.
4. The number of available observations was used as a tie-breaker.
5. The **top 20 games** from each interaction profile were selected for characterization.

This procedure produced an initial sample of:

**9 profiles × 20 games = 180 selected games**

Games for which the required gameplay characteristics could not be reliably verified were subsequently excluded.

The final gameplay-characterization sample contains:

**176 games**

The complete selected-game lists and the outputs documenting selection for each interaction profile are included in this folder.

---

## Gameplay Characterization

Each retained game was manually characterized across **eight gameplay dimensions**.

The dimensions capture structural properties of play relevant to how advertising and in-app purchases may operate within different game contexts:

1. **Natural pause opportunities**
2. **Natural activity boundaries**
3. **Continuous active play**
4. **Sequential advancement**
5. **Activity-state persistence**
6. **Reset / contained development**
7. **Cross-activity accumulation**
8. **Capability development**

Characteristics were coded independently and are not mutually exclusive. A game may therefore exhibit multiple gameplay characteristics.

Gameplay characterization was based on available game information, including Google Play descriptions and store information, supplemented where necessary by official developer/publisher information and secondary gameplay sources used to verify gameplay structure.

The detailed characterization methodology and coding procedure are provided in `Methodology.docx`.

---

## Analytical Comparison

After characterization, the prevalence of each gameplay characteristic was compared across positive and negative interaction profiles separately for Ads and IAP.

The analysis therefore contrasts:

- positive Ads profiles vs. negative Ads profiles; and
- positive IAP profiles vs. negative IAP profiles.

This comparison identifies whether the gameplay characteristics associated with interaction direction differ between the two monetization mechanisms.

---

## Main Gameplay Pattern

The characterization reveals a broad contrast between two forms of play.

### Bounded and Interruptible Play

This form of play is characterized particularly by:

- natural pause opportunities;
- natural activity boundaries; and
- reset or contained development.

These characteristics are more strongly represented in **positive Ads profiles** and **negative IAP profiles**.

### Persistent and Investment-Oriented Play

This form of play is characterized particularly by:

- continuous active play;
- activity-state persistence;
- cross-activity accumulation; and
- capability development.

These characteristics are more strongly represented in **negative Ads profiles** and **positive IAP profiles**.

The results therefore reveal a cross-monetization reversal: gameplay characteristics associated with positive Ads interactions correspond broadly to those associated with negative IAP interactions, while characteristics associated with negative Ads interactions correspond broadly to those associated with positive IAP interactions.

Sequential advancement is an exception to this broader crossover pattern, occurring more frequently in negative profiles for both monetization mechanisms.

---

## Files in This Folder

### Methodology and Characterization

`Methodology.docx`  
Detailed methodology used for game selection and gameplay characterization.

`Selected_Games.docx`  
Selected games used in the gameplay-characterization stage.

`Complete_Selected_Game_Lists_180_42_Countries.docx`  
Complete game-selection lists documenting the initial 180-game selection across the nine interaction profiles.

### Game-Selection Outputs

The following files document the game-selection output for each interaction profile:

- `Game_Selection_Output_Ads_Casual.png`
- `Game_Selection_Output_Ads_Puzzle.png`
- `Game_Selection_Output_Ads_RPG_negative.png`
- `Game_Selection_Output_Ads_Strategy_negative.png`
- `Game_Selection_Output_IAP_Casual_negative.png`
- `Game_Selection_Output_IAP_Puzzle_negative.png`
- `Game_Selection_Output_IAP_RPG.png`
- `Game_Selection_Output_IAP_Simulation.png`
- `Game_Selection_Output_IAP_Strategy.png`

Together, these nine files document the selection of the top games for each profile.

### Supporting Analysis Materials

`selection_code.png`  
Code used to implement the game-selection procedure.

---

