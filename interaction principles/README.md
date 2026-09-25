# Interaction Principles for Game Research

This methodological companion explains the interaction principles used in the **Interaction-Analysis Framework for Game Research**. The framework examines whether an empirical relationship observed in game-marketplace data remains equivalent when the context changes. In the accompanying study, this question is applied to monetization and marketplace success across gameplay, national-market, and temporal contexts.

The central distinction is between documenting that outcomes differ across contexts and testing whether the **relationship connecting an exposure to an outcome changes across those contexts**. Evidence established in one setting does not, by itself, establish that the same relationship has the same direction or magnitude elsewhere.

> **Scope.** The concepts below concern statistical interaction, effect modification, and effect-measure modification in observational data. They do not, by themselves, establish causal or mechanistic interaction.

## Notation

Throughout the examples:

- \(r\): focal feature or exposure, such as an Ads monetization feature
- \(\bar r\): absence/complement of \(r\)
- \(c\): contextual condition, such as a genre or national-market condition
- \(\bar c\): comparison context
- \(y\): outcome event, such as install success
- \(\bar y\): complement of the outcome

The four conditional outcome probabilities are:

| | c̄ | c |
|---|---:|---:|
| **r̄** | p<sub>y\|r̄c̄</sub> | p<sub>y\|r̄c</sub> |
| **r** | p<sub>y\|rc̄</sub> | p<sub>y\|rc</sub> |

---

# 1. Interaction, Effect Modification, and Effect-Measure Modification

## 1.1 Interaction

Interaction asks whether the relationship between \(r\) and \(y\) differs according to the level of \(c\). In this sense, the empirical relationship is **conditional on context** rather than represented adequately by a single pooled association.

The idea is not that \(r\) or \(c\) must independently be beneficial or harmful. The question is whether the observed association between \(r\) and \(y\) changes when \(c\) changes.

```text
                    Context c
                       │
                       ▼
Feature r ───────► Relationship ───────► Outcome y
                       │
             direction / magnitude
                 may change
```

In game research, \(r\) might represent Ads, \(c\) a game genre, and \(y\) marketplace success. An interaction is present on a specified effect scale when the Ads-success relationship differs between the compared genre contexts.

## 1.2 Effect Modification

In epidemiology, **effect modification** describes a situation in which an effect differs across levels of another variable. The modifier identifies contexts in which the estimated relationship is different. This makes effect modification directly relevant to research concerned with the contextual scope of empirical relationships.

For observational game-marketplace analyses, however, causal language should be used cautiously. When causal identification is not established, the safer interpretation is that the **measured association varies across contexts** rather than that the context modifies a causal effect.

See Knol and VanderWeele (2012) and Greenland (1983) for discussion of interaction and effect modification [1,2].

## 1.3 Effect-Measure Modification

**Effect-measure modification** makes the scale dependence explicit. A relationship may be homogeneous on one measure and heterogeneous on another. Consequently, interaction is not a single scale-free property of a dataset.

For example, the same four probabilities can yield:

- little or no departure from homogeneity on a probability-difference scale; and
- clear departure from homogeneity on an odds-ratio scale,

or the reverse.

The framework therefore evaluates interaction on two complementary scales:

- **DDP** — difference in probability differences, representing additive interaction;
- **RoR** — ratio of odds ratios, representing multiplicative interaction.

This dual-scale interpretation follows the epidemiological emphasis on specifying the effect measure when discussing interaction [1–5].

## 1.4 Three Concepts at a Glance

| Concept | Core question | Interpretation in this framework |
|---|---|---|
| **Interaction** | Does the relationship between \(r\) and \(y\) differ across \(c\)? | General contextual variation in a specified association |
| **Effect modification** | Does an effect differ across levels of a third variable? | Causal terminology only when causal assumptions are justified |
| **Effect-measure modification** | Does the measured association differ across \(c\) on a specified scale? | Preferred statistical framing for the observational analyses |

---

# 2. Additive and Multiplicative Interaction

## 2.1 Additive Interaction

On the probability-difference scale, first estimate the relationship between \(r\) and \(y\) within each context.

For context \(c\):

$$
PD_{r\mid c}=p_{y\mid rc}-p_{y\mid \bar r c}
$$

For context \(\bar c\):

$$
PD_{r\mid \bar c}=p_{y\mid r\bar c}-p_{y\mid \bar r\bar c}
$$

The additive interaction contrast is the **difference in probability differences**:

$$
\boxed{DDP=PD_{r\mid c}-PD_{r\mid \bar c}}
$$

The null value is:

$$
DDP=0.
$$

A non-zero DDP indicates that the probability-difference association between \(r\) and \(y\) is not homogeneous across the compared contexts.

### Numerical example

Suppose:

$$
PD_{r\mid c}=0.30, \qquad PD_{r\mid \bar c}=0.10.
$$

Then:

$$
DDP=0.30-0.10=0.20.
$$

The relationship is positive in both contexts, but it is 0.20 larger on the probability-difference scale under \(c\).

### Game-research translation

If \(r\) represents Ads, \(c\) represents RPG rather than a comparison genre context, and \(y\) represents install success, DDP asks whether the Ads-install-success probability difference changes when the gameplay context changes.

## 2.2 Multiplicative Interaction

For a probability \(p\), the corresponding odds are:

$$
o=\frac{p}{1-p}.
$$

Within context \(c\), the conditional odds ratio is:

$$
\theta_{yr\mid c}
=
\frac{o_{y\mid rc}}{o_{y\mid \bar r c}}.
$$

Within \(\bar c\):

$$
\theta_{yr\mid \bar c}
=
\frac{o_{y\mid r\bar c}}{o_{y\mid \bar r\bar c}}.
$$

The multiplicative interaction contrast is the **ratio of odds ratios**:

$$
\boxed{RoR=
\frac{\theta_{yr\mid c}}
{\theta_{yr\mid \bar c}}}
$$

The null value is:

$$
RoR=1.
$$

Thus, equal conditional odds ratios imply no multiplicative effect-measure modification, whereas unequal conditional odds ratios imply multiplicative heterogeneity.

## 2.3 Why the Two Scales Can Disagree

Additive and multiplicative interaction answer different questions. DDP compares **absolute probability differences**, whereas RoR compares **relative odds-ratio relationships**. Because these measures transform the underlying probabilities differently, evidence of interaction on one scale does not require evidence of interaction on the other.

Accordingly:

$$
DDP=0 \;\not\Rightarrow\; RoR=1,
$$

and

$$
RoR=1 \;\not\Rightarrow\; DDP=0.
$$

This is why reporting the scale is essential when describing interaction or homogeneity [1–5].

## 2.4 From Epidemiological Measures to the Framework

Epidemiological research has developed several measures for evaluating departure from additivity or multiplicativity, including the **relative excess risk due to interaction (RERI)**, attributable proportion due to interaction, synergy index, and regression product terms [5–8]. These measures formalize the general principle that interaction must be defined relative to a particular effect measure.

The present framework applies the same principle directly to conditional marketplace-success probabilities and odds:

$$
\text{Additive scale} \rightarrow DDP
$$

$$
\text{Multiplicative scale} \rightarrow RoR.
$$

DDP and RoR are therefore not intended as replacements for every epidemiological interaction measure. They are the study's chosen contrasts for evaluating whether the focal game-marketplace association changes across the examined contexts.

## 2.5 Why Both Scales Are Retained

Retaining both scales prevents a contextual relationship from being characterized from only one mathematical representation. Agreement across DDP and RoR provides stronger descriptive evidence that contextual heterogeneity is not confined to one effect scale. Disagreement is itself informative because it shows that the conclusion depends on how the relationship is measured.

---

# 3. Patterns of Interaction

## 3.1 Quantitative Interaction: Same Direction, Different Magnitude

A **quantitative interaction** occurs when the conditional relationships remain in the same direction but differ in magnitude.

For example:

$$
PD_{r\mid c}>0, \qquad PD_{r\mid \bar c}>0,
$$

but

$$
PD_{r\mid c}\neq PD_{r\mid \bar c}.
$$

If:

$$
PD_{r\mid c}=0.30, \qquad PD_{r\mid \bar c}=0.10,
$$

then:

$$
DDP=0.20.
$$

Both relationships are positive; the interaction concerns their unequal magnitude.

In a game-marketplace example, Ads could be positively associated with install success in two genre contexts but substantially more strongly in one than the other.

Importantly, **quantitative interaction is not synonymous with positive DDP**. If both conditional relationships are positive but the relationship under \(c\) is weaker, DDP will be negative even though neither relationship has changed direction. VanderWeele and Knol discuss the distinction between quantitative and qualitative interaction [5].

## 3.2 Qualitative / Crossover Interaction

A **qualitative** or **crossover interaction** occurs when the direction of the relationship changes across contexts. On the probability-difference scale:

$$
PD_{r\mid c}\times PD_{r\mid \bar c}<0.
$$

For example:

$$
PD_{r\mid c}=0.20,
\qquad
PD_{r\mid \bar c}=-0.20.
$$

Then:

$$
DDP=0.20-(-0.20)=0.40.
$$

The defining feature is not the size of DDP alone. It is the **opposite signs of the underlying conditional relationships**.

```text
Outcome
  ↑
  |        /  context c
  |       /
  |------X----------------
  |     /
  |    /   context c̄
  +----------------------→ r
```

In game research, a monetization feature may be positively associated with marketplace success under one gameplay context and negatively associated under another. This is a stronger form of contextual variation than a same-direction magnitude difference, but it remains an observational association unless causal assumptions are independently justified [5].

![Qualitative crossover interaction](example/crossover.png)

*Illustrative game-marketplace example of a qualitative/crossover interaction. The direction of the focal relationship differs across the compared contexts. The figure illustrates the statistical pattern rather than a causal mechanism.*

## 3.3 Amplification and Attenuation

**Amplification** and **attenuation** are useful descriptive labels for same-direction quantitative interaction. They describe whether the magnitude of the focal conditional relationship becomes stronger or weaker across contexts; they are not separate formal epidemiological interaction measures.

Amplification can be represented as:

$$
|PD_{r\mid c}|>|PD_{r\mid \bar c}|,
$$

whereas attenuation can be represented as:

$$
|PD_{r\mid c}|<|PD_{r\mid \bar c}|.
$$

The absolute values matter. If the underlying relationships are negative, a more negative probability difference represents amplification in magnitude even though DDP may itself be negative. Conversely, movement toward zero represents attenuation.

The same logic applies multiplicatively. The two conditional odds ratios should be inspected relative to the null value of 1 rather than interpreting RoR alone as automatically indicating amplification or attenuation.

In a game example, the association between a free-game characteristic and marketplace success may become stronger or weaker when IAP is present. The interpretation concerns the conditional association, not a causal claim about why it changes.

![Amplification pattern](example/freeIAP.jpg)

*Illustrative game-marketplace example of amplification. The figure shows a stronger conditional relationship under one context than another and is intended to demonstrate the interaction pattern rather than a primary empirical result.*

---

# 4. Homogeneity and Conditional Independence

## 4.1 Homogeneous Association

**Homogeneity** means that the association is equivalent across levels of the contextual variable on the specified effect measure. It does **not** require the association itself to be null.

On the odds-ratio scale:

$$
\theta_{yr\mid c}=\theta_{yr\mid \bar c}.
$$

For example:

$$
\theta_{yr\mid c}=2,
\qquad
\theta_{yr\mid \bar c}=2.
$$

The relationship is non-null in both contexts, but it is homogeneous on the odds-ratio scale. Equivalently:

$$
RoR=1.
$$

On the probability-difference scale, homogeneity corresponds to:

$$
PD_{r\mid c}=PD_{r\mid \bar c},
$$

and therefore:

$$
DDP=0.
$$

Homogeneity is scale-specific. A relationship can be homogeneous on one measure and heterogeneous on another [9,10].

For example, if \(r\) represents Ads, \(c\) genre context, and \(y\) install success, homogeneity means that the Ads-install relationship is equivalent across the compared genre contexts on the measure being examined.

## 4.2 Conditional Independence

**Conditional independence** is a stronger condition. It means that the relationship between \(r\) and \(y\) is absent after conditioning on \(c\):

$$
y\perp r\mid c.
$$

Within context \(c\):

$$
p_{y\mid rc}=p_{y\mid \bar r c},
$$

and within \(\bar c\):

$$
p_{y\mid r\bar c}=p_{y\mid \bar r\bar c}.
$$

Therefore:

$$
PD_{r\mid c}=PD_{r\mid \bar c}=0,
$$

and on the odds-ratio scale:

$$
\theta_{yr\mid c}=\theta_{yr\mid \bar c}=1.
$$

Conditional independence is therefore a special case of homogeneous conditional association in which the common association is null.

This distinction is crucial. A null interaction contrast does not imply conditional independence. For example:

$$
PD_{r\mid c}=PD_{r\mid \bar c}=0.20
$$

produces \(DDP=0\), yet a positive association remains in both contexts. Likewise:

$$
\theta_{yr\mid c}=\theta_{yr\mid \bar c}=2
$$

produces \(RoR=1\), but the conditional association is not null.

A marginal relationship can also coexist with conditional independence. For example, if \(r\) is Ads, \(c\) an age-rating group, and \(y\) install success, a pooled Ads-install association may be visible even when no association is observed within the examined age-rating strata.

![Conditional independence](example/conditional-independence.jpg)

*Illustrative game-marketplace example of conditional independence. A relationship is visible in the marginal comparison but is not observed within the examined age-rating strata. The example illustrates the distinction between marginal association and conditional association; it does not assign a causal explanation to the contextual variable.*

## 4.3 Homogeneity ≠ Conditional Independence

| Pattern | Probability-difference scale | Odds-ratio scale |
|---|---|---|
| **Homogeneous association** | PD<sub>r\|c</sub> = PD<sub>r\|c̄</sub> | θ<sub>yr\|c</sub> = θ<sub>yr\|c̄</sub> |
| **Conditional independence** | PD<sub>r\|c</sub> = PD<sub>r\|c̄</sub> = 0 | θ<sub>yr\|c</sub> = θ<sub>yr\|c̄</sub> = 1 |

Three simple cases make the distinction explicit:

```text
A. Homogeneous, non-independent:  ORc = 2.0, ORc̄ = 2.0
B. Homogeneous and independent:  ORc = 1.0, ORc̄ = 1.0
C. Heterogeneous:                ORc = 1.2, ORc̄ = 2.0
```

Thus, **no interaction** means that the specified association measure does not vary across the compared contexts. **Conditional independence** means that the conditional association itself is absent.

---

# 5. Marginal and Conditional Relationships

## 5.1 Marginal versus Conditional Association

A **marginal association** compares \(r\) and \(y\) without conditioning on \(c\). On the probability-difference scale:

$$
PD_r=p_{y\mid r}-p_{y\mid \bar r}.
$$

On the odds-ratio scale:

$$
\theta_{yr}=\frac{o_{y\mid r}}{o_{y\mid \bar r}}.
$$

Conditional associations instead compare \(r\) and \(y\) separately within \(c\) and \(\bar c\), producing \(PD_{r\mid c}\), \(PD_{r\mid \bar c}\), \(\theta_{yr\mid c}\), and \(\theta_{yr\mid \bar c}\).

The marginal probability is a mixture of conditional probabilities. For example:

$$
P(y\mid r)
=
P(y\mid r,c)P(c\mid r)
+
P(y\mid r,\bar c)P(\bar c\mid r).
$$

Similarly:

$$
P(y\mid \bar r)
=
P(y\mid \bar r,c)P(c\mid \bar r)
+
P(y\mid \bar r,\bar c)P(\bar c\mid \bar r).
$$

The marginal relationship therefore depends both on the conditional outcome probabilities and on how observations are distributed across the contextual variable.

Several patterns are possible: marginal and conditional relationships may agree; their magnitudes may differ; a marginal relationship may disappear after conditioning; or its direction may reverse.

For example, with \(r\)=Ads, \(c\)=country, and \(y\)=install success, a pooled cross-market association need not reproduce the association observed within each national market.

Importantly, **not every difference between marginal and conditional estimates is Simpson's paradox**.

## 5.2 Simpson's Paradox

**Simpson's paradox** refers specifically to a reversal in the direction of a relationship between an aggregated comparison and the corresponding conditional comparisons.

For example:

$$
PD_r>0,
$$

while:

$$
PD_{r\mid c}<0
\qquad\text{and}\qquad
PD_{r\mid \bar c}<0.
$$

An illustrative configuration is:

$$
PD_r=+0.10,
$$

but:

$$
PD_{r\mid c}=-0.10,
\qquad
PD_{r\mid \bar c}=-0.10.
$$

The pooled relationship is positive even though the relationship within both examined strata is negative. A comparable reversal can occur on the odds-ratio scale, for example with a marginal odds ratio above 1 and conditional odds ratios below 1.

This reversal arises because aggregation combines conditional outcome probabilities with the distribution of observations across \(c\). The statistical pattern should not automatically be assigned a causal explanation.

The distinction from interaction is fundamental:

```text
Interaction:
Does the conditional relationship differ between c and c̄?

Simpson-type reversal:
Does the marginal direction differ from the conditional direction(s)?
```

A Simpson-type reversal can occur even when the conditional relationships are homogeneous. In the numerical example above, both conditional probability differences are \(-0.10\), so \(DDP=0\), despite the reversal between the pooled and conditional comparisons.

Simpson's paradox is also different from conditional independence. Under conditional independence, the within-stratum relationships are null. Under a Simpson-type reversal, the conditional relationships are non-null and point in the opposite direction from the marginal relationship.

In game research, \(r\) could represent a monetization feature, \(c\) game genre, and \(y\) marketplace success. A pooled relationship may point in one direction while the genre-specific relationships point in the other.

![Simpson's paradox](example/fallacy.png)

*Illustrative game-marketplace example of an aggregation reversal. The direction observed in the pooled comparison differs from the direction observed within the examined contextual strata. The figure illustrates a marginal-conditional reversal and should not, by itself, be interpreted as evidence of interaction or as establishing a causal explanation.*

---

# 6. Suppression-Type Patterns and Revealed Conditional Relationships

## 6.1 Suppression

The term **suppression** has been used in several related statistical traditions, including regression, mediation, confounding, and epidemiologic discussions of reversal phenomena. It should therefore be used with an explicit operational definition rather than treated as a universally standardized interaction category.

In the descriptive sense used here, a **suppression-type pattern** occurs when a marginal relationship is weak or close to null, but a stronger relationship becomes visible after conditioning on a contextual variable.

A simple probability-difference pattern is:

$$
PD_r\approx0,
$$

while at least one conditional relationship satisfies:

$$
|PD_{r\mid c}|>|PD_r|
$$

or

$$
|PD_{r\mid \bar c}|>|PD_r|.
$$

The same idea can be expressed using other association measures: conditioning reveals or strengthens a relationship that was obscured in the aggregate comparison. In regression terminology, suppression commonly refers to situations in which including another variable increases the predictive or estimated contribution of a focal predictor. MacKinnon, Krull, and Lockwood discuss the close relationships among mediation, confounding, and suppression effects [11].

For this framework, **suppression-type pattern** is intentionally descriptive. It identifies a marginal-to-conditional change and does not imply that the contextual variable has been established as the causal reason for that change.

## 6.2 Suppression versus Interaction

Suppression and interaction compare different quantities.

```text
Suppression-type pattern
Marginal relationship  ↔  Conditional relationship

Interaction
Conditional relationship under c  ↔  Conditional relationship under c̄
```

A relationship can therefore be revealed after conditioning without necessarily showing interaction between the conditional strata. Conversely, strong interaction can occur even when the marginal relationship is not suppressed.

Suppose:

$$
PD_r\approx0,
$$

but:

$$
PD_{r\mid c}=0.20,
\qquad
PD_{r\mid \bar c}=0.20.
$$

The conditional relationship is stronger than the marginal relationship, but:

$$
DDP=0.20-0.20=0.
$$

Thus, a suppression-type marginal-to-conditional pattern can coexist with homogeneous conditional relationships.

## 6.3 Suppression versus Simpson's Paradox

The distinction is whether the primary marginal-to-conditional change is **revelation/strengthening** or **direction reversal**.

| Pattern | Marginal relationship | Conditional relationship |
|---|---|---|
| **Suppression-type** | Weak, attenuated, or near null | Stronger/revealed after conditioning |
| **Simpson-type reversal** | Points in one direction | Points in the opposite direction within the relevant strata |

A suppression-type pattern does not require a sign reversal. Simpson's paradox does.

Because the term suppression is used differently across disciplines, analyses should report the actual marginal and conditional estimates rather than relying on the label alone.

## 6.4 Game-Data Example

In a game-marketplace setting, a monetization-success relationship may appear weak when games are pooled, while a clearer association becomes visible after conditioning on a relevant game characteristic. This can occur because the aggregate comparison combines observations from contexts with different compositions or relationships.

![Suppression-type pattern](example/suppression.png)

*Illustrative game-marketplace example of a suppression-type pattern. A relationship that is weak or obscured in the aggregate comparison becomes more apparent after conditioning on the examined context. The figure is descriptive and does not establish that the contextual variable causally produces the change.*

---

# 7. Interpretation Guide

The concepts above can be organized around two separate comparisons: **conditional-to-conditional** comparisons, which evaluate interaction, and **marginal-to-conditional** comparisons, which evaluate how aggregation changes the observed relationship.

```text
START WITH THE CONDITIONAL RELATIONSHIPS

Do the r-y relationships differ across c and c̄?
│
├── YES → Heterogeneity / interaction on the specified scale
│          │
│          ├── Same direction, different magnitude
│          │      → Quantitative interaction
│          │      → May be described as amplification/attenuation
│          │
│          └── Opposite directions
│                 → Qualitative / crossover interaction
│
└── NO → Homogeneous association on the specified scale
           │
           ├── Common relationship is non-null
           │      → Homogeneous non-null association
           │
           └── Common relationship is null
                  → Conditional independence

THEN COMPARE MARGINAL AND CONDITIONAL RELATIONSHIPS

Does conditioning materially change what is observed?
│
├── Marginal association disappears within strata
│      → Conditional-independence pattern, if conditional associations are null
│
├── Direction reverses
│      → Simpson-type reversal
│
└── Weak/obscured marginal relationship becomes stronger
       → Suppression-type pattern
```

The key principle is that **contextual variation in outcomes is not the same as contextual variation in relationships**. A country, genre, player group, or time period may have a different outcome level without modifying the focal relationship. Interaction analysis therefore asks a more specific question: whether the measured relationship itself persists, weakens, strengthens, or changes direction as context changes.

This distinction is central to establishing the **contextual scope of empirical evidence**. A relationship demonstrated in one setting is evidence for that setting; generalization beyond it requires examining whether the relationship recurs under the additional contexts to which the conclusion is being extended.

---

# References

1. Knol MJ, VanderWeele TJ. Recommendations for presenting analyses of effect modification and interaction. *International Journal of Epidemiology*. 2012;41(2):514–520. DOI: [10.1093/ije/dyr218](https://doi.org/10.1093/ije/dyr218)

2. Greenland S. Tests for interaction in epidemiologic studies: a review and a study of power. *Statistics in Medicine*. 1983;2(2):243–251. DOI: [10.1002/sim.4780020219](https://doi.org/10.1002/sim.4780020219)

3. Greenland S. Effect Modification and Interaction. *Wiley StatsRef: Statistics Reference Online*. DOI: [10.1002/9781118445112.stat03728.pub2](https://doi.org/10.1002/9781118445112.stat03728.pub2)

4. Brumback BA. Discussion of “Estimating measures of interaction on an additive scale for preventive exposures.” *Statistics in Medicine*. 2008. DOI: [10.1002/sim.3246](https://doi.org/10.1002/sim.3246)

5. VanderWeele TJ, Knol MJ. A Tutorial on Interaction. *Epidemiologic Methods*. 2014;3(1):33–72. DOI: [10.1515/em-2013-0005](https://doi.org/10.1515/em-2013-0005)

6. Andersson T, Alfredsson L, Källberg H, Zdravkovic S, Ahlbom A. Calculating measures of biological interaction. *European Journal of Epidemiology*. 2005;20(7):575–579. DOI: [10.1007/s10654-005-7835-x](https://doi.org/10.1007/s10654-005-7835-x)

7. Richardson DB, Kaufman JS. Estimation of the relative excess risk due to interaction and associated confidence bounds. *American Journal of Epidemiology*. 2009;169(6):756–760. DOI: [10.1093/aje/kwn411](https://doi.org/10.1093/aje/kwn411)

8. Knol MJ, VanderWeele TJ, Groenwold RHH, Klungel OH, Rovers MM, Grobbee DE. Estimating measures of interaction on an additive scale for preventive exposures. *European Journal of Epidemiology*. 2011;26:433–438. DOI: [10.1007/s10654-011-9554-9](https://doi.org/10.1007/s10654-011-9554-9)

9. Greenland S. Interpretation and estimation of summary ratios under heterogeneity. *Statistics in Medicine*. 1982;1(3):217–227. DOI: [10.1002/sim.4780010304](https://doi.org/10.1002/sim.4780010304)

10. Mantel N, Brown C, Byar DP. Tests for homogeneity of effect in an epidemiologic investigation. *American Journal of Epidemiology*. 1977;106(2):125–129. DOI: [10.1093/oxfordjournals.aje.a112441](https://doi.org/10.1093/oxfordjournals.aje.a112441)

11. MacKinnon DP, Krull JL, Lockwood CM. Equivalence of the mediation, confounding and suppression effect. *Prevention Science*. 2000;1(4):173–181. DOI: [10.1023/A:1026595011371](https://doi.org/10.1023/A:1026595011371)
