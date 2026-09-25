# Interaction Principles

The **Interaction-Analysis Framework** developed in this research draws on established principles of interaction and effect-measure modification from epidemiology and translates them to contextual questions in game research.

The central principle is that an empirical relationship observed overall does not necessarily remain equivalent across the conditions in which it is observed.

> **Core idea:**  
> A relationship can strengthen, weaken, disappear, or change direction across contexts.

This page develops these principles progressively. Each concept is introduced from the methodological literature, expressed statistically, translated to the game-research setting, and, where appropriate, illustrated using game-marketplace examples.

---

# 1. Interaction, Effect Modification, and Effect-Measure Modification

The epidemiological literature uses **interaction**, **effect modification**, and **effect-measure modification** for closely related but distinguishable ideas.

A useful starting point is to distinguish whether the question concerns the **joint relationship of two factors** or whether the relationship of **one focal factor varies across levels of another factor**.

```text
                         CONTEXTUAL DEPENDENCE
                                  │
                 ┌────────────────┴────────────────┐
                 │                                 │
                 ▼                                 ▼
        JOINT RELATIONSHIP                 STRATUM-SPECIFIC
           OF A AND B                     RELATIONSHIP OF A
                 │                                 │
                 ▼                                 ▼
           INTERACTION                    EFFECT MODIFICATION
                                                   │
                                                   ▼
                                      EFFECT-MEASURE MODIFICATION
                                      when defined for a specific
                                             effect measure
```

Knol and VanderWeele distinguish these analytical questions by separating the examination of the effect of one exposure across strata of another factor from examination of the joint effects of two exposures.

**Methodological source:**  
Knol MJ, VanderWeele TJ. *Recommendations for presenting analyses of effect modification and interaction.* International Journal of Epidemiology. 2012;41(2):514–520.  
**[DOI: 10.1093/ije/dyr218](https://doi.org/10.1093/ije/dyr218)**

---

## 1.1 Interaction

### The principle

**Interaction concerns the joint relationship of two factors with an outcome and whether that joint relationship departs from a specified no-interaction reference.**

Let:

- \(r\) = first factor
- \(c\) = second factor
- \(y\) = outcome

For two binary factors, four joint conditions are possible:

| | c̄ | c |
|---|---:|---:|
| **r̄** | p<sub>y\|r̄c̄</sub> | p<sub>y\|r̄c</sub> |
| **r** | p<sub>y\|rc̄</sub> | p<sub>y\|rc</sub> |

where

```math
p_{y\mid rc}=P(y\mid r,c).
```

Thus,

```math
p_{y\mid\bar r\bar c}=P(y\mid\bar r,\bar c)
```

is the outcome probability when neither factor is present, whereas

```math
p_{y\mid rc}=P(y\mid r,c)
```

is the outcome probability when both factors are present.

These four conditions provide the basic structure from which interaction can be evaluated.

### What makes it an interaction?

A large value of \(p_{y\mid rc}\) is **not, by itself, evidence of interaction**.

The critical question is whether the observed joint relationship differs from the relationship expected from the separate relationships of \(r\) and \(c\) under a specified **no-interaction model**.

```text
Observed joint relationship
           │
           ▼
          P₁₁
           │
           │ compare with
           ▼
Expected joint relationship
under a no-interaction model
           │
           ▼
 Departure from expectation?
       /               \
     NO                 YES
     │                   │
No interaction       Interaction
on that scale        on that scale
```

What counts as the expected joint relationship depends on the **scale** on which interaction is evaluated.

---

### Additive reference

On the probability-difference scale, the individual relationships associated with \(r\) and \(c\) can be written as

```math
PD_r=p_{y\mid r\bar c}-p_{y\mid\bar r\bar c}
```

and

```math
PD_c=p_{y\mid\bar r c}-p_{y\mid\bar r\bar c}.
```

Under an additive no-interaction model, the expected joint probability is

```math
p_{y\mid rc}^{(\mathrm{expected})}
=
p_{y\mid r\bar c}+p_{y\mid\bar r c}-p_{y\mid\bar r\bar c}.
```

The departure from additivity is therefore

```math
IC_{\mathrm{add}}
=
p_{y\mid rc}-p_{y\mid r\bar c}-p_{y\mid\bar r c}+p_{y\mid\bar r\bar c}.
```

The additive null is

```math
IC_{\mathrm{add}}=0.
```

A non-zero value represents departure from the additive no-interaction reference.

---

### Multiplicative reference

A different reference is obtained when relationships are represented on a relative scale.

For example, using risk ratios,

```math
RR_{10}=\frac{p_{y\mid r\bar c}}{p_{y\mid\bar r\bar c}},
\qquad
RR_{01}=\frac{p_{y\mid\bar r c}}{p_{y\mid\bar r\bar c}},
\qquad
RR_{11}=\frac{p_{y\mid rc}}{p_{y\mid\bar r\bar c}}.
```

Under a multiplicative no-interaction model,

```math
RR_{11}^{(\mathrm{expected})}
=
RR_{10}\times RR_{01}.
```

Departure from multiplicativity can therefore be represented by

```math
IC_{\mathrm{mult}}
=
\frac{RR_{11}}
     {RR_{10}RR_{01}}.
```

The multiplicative null is

```math
IC_{\mathrm{mult}}=1.
```

This leads to an important principle:

> **Interaction is scale dependent.**

```text
                 SAME FOUR JOINT CONDITIONS
                           │
                    p(y|r̄c̄) p(y|rc̄) p(y|r̄c) p(y|rc)
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
       ADDITIVE SCALE             MULTIPLICATIVE SCALE
             │                           │
       No interaction:             No interaction:
             0                           1
             │                           │
             └─────────────┬─────────────┘
                           ▼
                   Conclusions need
                  not be equivalent
```

The same data can therefore show departure from additivity, departure from multiplicativity, departure from both, or departure from neither.

**Methodological sources:**  

Greenland S. *Tests for interaction in epidemiologic studies: A review and a study of power.* Statistics in Medicine. 1983;2(2):243–251.  
**[DOI: 10.1002/sim.4780020219](https://doi.org/10.1002/sim.4780020219)**

Knol MJ, VanderWeele TJ. *Recommendations for presenting analyses of effect modification and interaction.* International Journal of Epidemiology. 2012;41(2):514–520.  
**[DOI: 10.1093/ije/dyr218](https://doi.org/10.1093/ije/dyr218)**

---

### Translation to game research

The same structure can be used when \(r\) and \(c\) represent characteristics of games rather than epidemiological exposures.

For example:

```text
r = Free
c = Offers IAP
y = Marketplace success
```
This gives four conditions:

| | No IAP (c̄) | IAP (c) |
|---|---:|---:|
| **Not Free (r̄)** | p<sub>y\|r̄c̄</sub> | p<sub>y\|r̄c</sub> |
| **Free (r)** | p<sub>y\|rc̄</sub> | p<sub>y\|rc</sub> |

The interaction question is **not simply whether Free + IAP games have high marketplace success**.

Instead, the question is:

> **Is the joint Free × IAP relationship with marketplace success different from what would be expected from the separate Free and IAP relationships under the specified interaction scale?**

This distinction becomes important when specific interaction patterns are introduced later on this page.

---

## 1.2 Effect Modification

Interaction can focus on the joint relationship of two factors. **Effect modification changes the orientation of the question.**

Suppose:

- \(r\) = focal factor
- \(c\) = modifying factor
- \(y\) = outcome

Instead of primarily evaluating the joint \(r \times c\) relationship, the relationship between \(r\) and \(y\) is examined within different levels of \(c\):

```math
M(r,y\mid\bar c)
```

versus

```math
M(r,y\mid c).
```

Conceptually:

```text
                     A ─────────────► Y
                     │
                     │
              Does this relationship
                  depend on X?
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
        X = 0                 X = 1
          │                     │
          ▼                     ▼
     A ─────► Y            A ─────────► Y
      relationship          relationship
          │                     │
          └──────────┬──────────┘
                     ▼
                   Compare
```

If the relationship differs across levels of \(c\), the \(r\)–\(y\) relationship is modified across \(c\).

The conceptual distinction can therefore be expressed as:

```text
INTERACTION

"What happens when r and c occur jointly?"

                    versus

EFFECT MODIFICATION

"Does the r–y relationship differ across levels of c?"
```

**Methodological source:**  
Knol MJ, VanderWeele TJ. *Recommendations for presenting analyses of effect modification and interaction.* International Journal of Epidemiology. 2012;41(2):514–520.  
**[DOI: 10.1093/ije/dyr218](https://doi.org/10.1093/ije/dyr218)**

---

### Translation to game research

Let:

```text
r = Ads
c = Game genre
y = Marketplace success
```

The question becomes:

> **Does the Ads–marketplace-success relationship differ across game genres?**

Conceptually:

```text
                    ADS
                     │
                     ▼
             MARKETPLACE SUCCESS
                     │
              examined within
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
     Puzzle         RPG         Strategy
       │             │             │
   Ads–success   Ads–success   Ads–success
   relationship  relationship  relationship
       │             │             │
       └─────────────┼─────────────┘
                     ▼
          Are they equivalent?
```

The same question can be extended to other contexts:

```text
Ads ──► Success | Genre

Ads ──► Success | Country

Ads ──► Success | Time
```

The substantive question is therefore no longer merely whether Ads and marketplace success are associated overall, but whether the observed relationship is **context dependent**.

---

## 1.3 Effect-Measure Modification

The term **effect-measure modification (EMM)** makes an important additional distinction.

What varies across contexts is a **specified measure of the relationship**.

Greenland distinguishes variation in a chosen effect measure across levels of a background variable as **effect-measure modification**.

**Methodological source:**  
Greenland S. *Effect Modification and Interaction.* Wiley StatsRef: Statistics Reference Online.  
**[DOI: 10.1002/9781118445112.stat03728.pub2](https://doi.org/10.1002/9781118445112.stat03728.pub2)**

### Formal representation

Let \(M\) denote a chosen measure of the \(r\)–\(y\) relationship.

Effect-measure modification can be represented as

```math
M(r,y\mid\bar c)
\neq
M(r,y\mid c).
```

More generally, across \(K\) contexts:

```math
M(r,y\mid c),\;
M(r,y\mid c_2),\;
\dots,\;
M(r,y\mid c_K)
```

need not be homogeneous.

The important point is that the conclusion depends on **what \(M\) represents**.

For example,

```math
M_{\mathrm{add}}
=
\text{Probability Difference}
```

and

```math
M_{\mathrm{mult}}
=
\text{Relative Measure}
```

represent the relationship on different scales.

Therefore:

```text
                    A ─────► Y
                        │
                  conditioned on X
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
       ADDITIVE MEASURE     MULTIPLICATIVE MEASURE
             │                     │
       M_add(r,y|c)          M_mult(r,y|c)
             │                     │
             └──────────┬──────────┘
                        ▼
              Contextual conclusions
                can differ by scale
```

A relationship can therefore exhibit effect-measure modification on one scale without exhibiting the same pattern on another scale.

This is why specifying the measure is important rather than simply stating that an "effect is modified."

**Methodological source:**  
Brumback BA. *On effect-measure modification: Relationships among changes in the relative risk, odds ratio, and risk difference.* Statistics in Medicine. 2008;27(18):3453–3465.  
**[DOI: 10.1002/sim.3246](https://doi.org/10.1002/sim.3246)**

---

### Translation to the Interaction-Analysis Framework

This distinction is particularly important for the present framework.

The observational question is not simply:

> *Does monetization work differently in different contexts?*

Rather, it is:

> **Does the measured relationship between monetization and marketplace success vary across the contexts represented in the data?**

For example:

```text
                    ADS
                     │
                     ▼
               INSTALL SUCCESS
                     │
              examined across
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
     Genre         Country         Time
       │             │             │
       └─────────────┼─────────────┘
                     ▼
              MEASURED ON
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       ADDITIVE             MULTIPLICATIVE
         DDP                     RoR
          │                       │
          └──────────┬────────────┘
                     ▼
             CONTEXTUAL PROFILE
```

The framework therefore evaluates contextual variation on both additive and multiplicative scales rather than assuming that a relationship characterized on one measure fully describes its contextual behavior.

---

## 1.4 The Three Concepts at a Glance

```text
┌──────────────────────────────────────────────────────────────┐
│                         INTERACTION                          │
│                                                              │
│  Do r and c jointly depart from the relationship expected   │
│  from their separate relationships on a specified scale?    │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                    EFFECT MODIFICATION                       │
│                                                              │
│  Does the relationship between r and y differ across        │
│  levels of c?                                               │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                EFFECT-MEASURE MODIFICATION                   │
│                                                              │
│  Does a specified measure of the r–y relationship differ    │
│  across levels of c?                                        │
└──────────────────────────────────────────────────────────────┘
```

These concepts provide the foundation for the interaction principles developed in the following sections.

The next step is to distinguish **additive and multiplicative interaction**, define the corresponding **no-interaction reference on each scale**, and examine how departures from those references can be interpreted.

---

# 2. Additive and Multiplicative Interaction

Interaction has no single scale-independent definition. The same four outcome
probabilities can be compared using different reference models, and the
conclusion about interaction can depend on the scale chosen.

For the two factors \(r\) and \(c\), the four success probabilities are:

| | c̄ | c |
|---|---:|---:|
| **r̄** | p<sub>y\|r̄c̄</sub> | p<sub>y\|r̄c</sub> |
| **r** | p<sub>y\|rc̄</sub> | p<sub>y\|rc</sub> |

The question is not simply whether these probabilities differ. The question is
whether the relationship associated with \(r\) changes across \(c\), relative
to a particular **no-interaction reference**.

```text
                         SAME FOUR PROBABILITIES
                                  │
                                  ▼
                 What counts as "no interaction"?
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
             ADDITIVE SCALE              MULTIPLICATIVE SCALE
                    │                           │
             Differences are                Ratios are
                compared                     compared
                    │                           │
                    ▼                           ▼
               Null = 0                     Null = 1
```
This distinction between additive and multiplicative interaction is well
established in epidemiological methodology, where evidence of interaction
can depend on the scale on which the joint relationship is evaluated.

**Methodological source:**  
VanderWeele TJ, Knol MJ. *A Tutorial on Interaction.* Epidemiologic Methods.
2014;3(1):33–72.  
**[DOI: 10.1515/em-2013-0005](https://doi.org/10.1515/em-2013-0005)**
---

## 2.1 Additive Interaction

### Comparing differences

On the additive scale, the relationship is expressed as an **absolute
difference in outcome probabilities**.

Within \(c\), the probability difference associated with \(r\) is:

```math
PD_{r\mid c}
=
p_{y\mid rc}
-
p_{y\mid\bar r c}.
```

Within \(\bar c\), the corresponding probability difference is:

```math
PD_{r\mid\bar c}
=
p_{y\mid r\bar c}
-
p_{y\mid\bar r\bar c}.
```

Additive interaction asks whether these two differences are equal:

```math
PD_{r\mid c}
\stackrel{?}{=}
PD_{r\mid\bar c}.
```

Their difference gives the **difference in differences of probabilities
(DDP)**:

```math
\mathrm{DDP}
=
PD_{r\mid c}
-
PD_{r\mid\bar c}.
```

Expanding the expression:

```math
\mathrm{DDP}
=
\left(
p_{y\mid rc}
-
p_{y\mid\bar r c}
\right)
-
\left(
p_{y\mid r\bar c}
-
p_{y\mid\bar r\bar c}
\right).
```

Equivalently:

```math
\boxed{
\mathrm{DDP}
=
p_{y\mid rc}
-
p_{y\mid\bar r c}
-
p_{y\mid r\bar c}
+
p_{y\mid\bar r\bar c}
}
```

The additive no-interaction condition is:

```math
\boxed{\mathrm{DDP}=0}
```

because this means:

```math
PD_{r\mid c}
=
PD_{r\mid\bar c}.
```

In other words, the absolute probability difference associated with \(r\)
is the same whether \(c\) is present or absent.

---

### Reading the additive scale

```text
DDP < 0                    DDP = 0                    DDP > 0
   │                          │                          │
   ▼                          ▼                          ▼
Negative departure       No departure             Positive departure
from additivity          from additivity           from additivity
```

Thus, the sign of DDP describes the **direction of departure from the
additive reference**.

Importantly, a positive DDP does not simply mean that the joint group has a
high probability of success, and a negative DDP does not simply mean that it
has a low probability.

The quantity describes how far the observed joint pattern departs from the
pattern expected under additivity.

---

### A simple numerical example

Suppose:

```math
p_{y\mid\bar r\bar c}=0.20,
\qquad
p_{y\mid r\bar c}=0.30,
```

```math
p_{y\mid\bar r c}=0.40,
\qquad
p_{y\mid rc}=0.65.
```

The relationship associated with \(r\) when \(c\) is absent is:

```math
PD_{r\mid\bar c}
=
0.30-0.20
=
0.10.
```

When \(c\) is present:

```math
PD_{r\mid c}
=
0.65-0.40
=
0.25.
```

Therefore:

```math
\mathrm{DDP}
=
0.25-0.10
=
0.15.
```

The positive value indicates that the probability difference associated with
\(r\) is **0.15 larger in the presence of \(c\)** than in its absence.

Visually:

```text
                     r̄                     r
                     │                      │

c̄                  0.20 ───── +0.10 ───► 0.30

c                   0.40 ───── +0.25 ───► 0.65
                                     
                         difference
                         in differences
                              │
                              ▼
                         0.25 - 0.10
                              │
                              ▼
                         DDP = +0.15
```

This is a **positive departure from additivity**.

---

### Game-research interpretation

Suppose:

```text
r = Ads
c = RPG
y = Install success
```

Then:

```math
PD_{r\mid c}
```

represents the Ads–install-success probability difference among RPG games,
whereas

```math
PD_{r\mid\bar c}
```

represents the corresponding Ads–install-success probability difference among
non-RPG games.

The DDP therefore asks:

> **How much does the Ads–install-success probability difference change when
> moving from non-RPG to RPG games?**

This provides an additive measure of contextual variation in the observed
Ads–success relationship.

---

## 2.2 Multiplicative Interaction

### Comparing relative relationships

The same four probabilities can be examined on a multiplicative scale.

In the present framework, the outcome probabilities are first transformed to
odds:

```math
o_{y\mid rc}
=
\frac{p_{y\mid rc}}
     {1-p_{y\mid rc}}.
```

Analogously:

```math
o_{y\mid\bar r c},
\qquad
o_{y\mid r\bar c},
\qquad
o_{y\mid\bar r\bar c}.
```

Within \(c\), the conditional odds ratio for the association between \(r\)
and \(y\) is:

```math
\theta_{yr\mid c}
=
\frac{o_{y\mid rc}}
     {o_{y\mid\bar r c}}.
```

Within \(\bar c\):

```math
\theta_{yr\mid\bar c}
=
\frac{o_{y\mid r\bar c}}
     {o_{y\mid\bar r\bar c}}.
```

Multiplicative interaction asks whether these conditional odds ratios are
equal:

```math
\theta_{yr\mid c}
\stackrel{?}{=}
\theta_{yr\mid\bar c}.
```

Their ratio gives the **ratio of odds ratios (RoR)**:

```math
\boxed{
\mathrm{RoR}
=
\frac{\theta_{yr\mid c}}
     {\theta_{yr\mid\bar c}}
}
```

The multiplicative no-interaction condition is:

```math
\boxed{\mathrm{RoR}=1}
```

because:

```math
\mathrm{RoR}=1
\iff
\theta_{yr\mid c}
=
\theta_{yr\mid\bar c}.
```

Thus, RoR evaluates whether the odds-ratio association between \(r\) and \(y\)
is homogeneous across the two conditions defined by \(c\).

---

### Reading the multiplicative scale

```text
RoR < 1                    RoR = 1                    RoR > 1
   │                          │                          │
   ▼                          ▼                          ▼
Negative departure       No departure             Positive departure
from multiplicativity    from multiplicativity     from multiplicativity
```

Again, these values describe **departure from the multiplicative reference**.
They should not be interpreted simply as low, neutral, or high marketplace
success.

---

## 2.3 Why the Two Scales Can Disagree

Additive and multiplicative interaction ask different mathematical questions.

```text
ADDITIVE

Does the probability difference change across c?

PD(r | c)  versus  PD(r | c̄)

              │
              ▼
             DDP


MULTIPLICATIVE

Does the odds ratio change across c?

OR(r,y | c)  versus  OR(r,y | c̄)

              │
              ▼
             RoR
```

Therefore:

```math
\mathrm{DDP}=0
```

does **not** mathematically require

```math
\mathrm{RoR}=1,
```

and conversely,

```math
\mathrm{RoR}=1
```

does not require

```math
\mathrm{DDP}=0.
```

This gives four possible analytical patterns:

| Additive scale | Multiplicative scale | Interpretation |
|---|---|---|
| DDP = 0 | RoR = 1 | No departure on either scale |
| DDP ≠ 0 | RoR = 1 | Departure from additivity only |
| DDP = 0 | RoR ≠ 1 | Departure from multiplicativity only |
| DDP ≠ 0 | RoR ≠ 1 | Departure on both scales |

The two measures should therefore be interpreted as **complementary
descriptions of the same four-cell probability structure**, rather than as
competing tests that must necessarily reach the same conclusion.

---

## 2.4 From Epidemiological Measures to the Present Framework

Epidemiological research has long emphasized that interaction can be evaluated
on different scales. Additive interaction is commonly represented using
measures such as the **relative excess risk due to interaction (RERI)**,
attributable proportion due to interaction, and synergy index, whereas
multiplicative interaction can be assessed through relative measures and
product terms.

The present framework follows the same underlying principle of
**scale-specific departure from a no-interaction reference**, but expresses
the two comparisons directly through:

```text
                  INTERACTION ANALYSIS
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
      ADDITIVE SCALE            MULTIPLICATIVE SCALE
             │                         │
             ▼                         ▼
            DDP                       RoR
             │                         │
       Null value = 0            Null value = 1
             │                         │
             └────────────┬────────────┘
                          ▼
                95% confidence intervals
                          │
                          ▼
               Context-specific profile
```

This distinction is important: **DDP and RoR are the measures used in this
framework**, while measures such as RERI belong to related epidemiological
formulations of additive interaction.

**Methodological sources:**  

Andersson T, Alfredsson L, Källberg H, Zdravkovic S, Ahlbom A.
*Calculating measures of biological interaction.* European Journal of Epidemiology.
2005;20(7):575–579.  
**[DOI: 10.1007/s10654-005-7835-x](https://doi.org/10.1007/s10654-005-7835-x)**

Richardson DB, Kaufman JS. *Estimation of the Relative Excess Risk Due to
Interaction and Associated Confidence Bounds.* American Journal of Epidemiology.
2009;169(6):756–760.  
**[DOI: 10.1093/aje/kwn411](https://doi.org/10.1093/aje/kwn411)**

Knol MJ, VanderWeele TJ, Groenwold RHH, Klungel OH, Rovers MM, Grobbee DE.
*Estimating measures of interaction on an additive scale for preventive
exposures.* European Journal of Epidemiology. 2011;26:433–438.  
**[DOI: 10.1007/s10654-011-9554-9](https://doi.org/10.1007/s10654-011-9554-9)**

Knol MJ, VanderWeele TJ. *Recommendations for presenting analyses of effect
modification and interaction.* International Journal of Epidemiology.
2012;41(2):514–520.  
**[DOI: 10.1093/ije/dyr218](https://doi.org/10.1093/ije/dyr218)**

---

## 2.5 Why Both Scales Are Retained

Using both scales allows the contextual pattern to be examined without making
one scale the sole definition of interaction.

For every contextual comparison, the framework therefore asks two parallel
questions:

```text
1. ADDITIVE
   Does the absolute probability difference vary across the context?
                         │
                         ▼
                        DDP


2. MULTIPLICATIVE
   Does the odds-ratio association vary across the context?
                         │
                         ▼
                        RoR
```

Together, these measures provide two complementary views of how an observed
relationship changes across context.

The next sections examine the **forms that these departures can take**,
including positive and negative departures, amplification and attenuation,
crossover patterns, conditional independence, and related contextual
structures.


# 3. Patterns of Interaction

Once interaction has been established as a departure from a specified
no-interaction reference, the next question concerns the **form of that
departure**.

Two distinctions are especially useful. First, the relationship may retain
the same direction across contexts while changing in magnitude. Second, the
relationship may change direction across contexts. These are commonly
described as **quantitative** and **qualitative (or crossover) interaction**,
respectively.

**Methodological source:**  
VanderWeele TJ, Knol MJ. *A Tutorial on Interaction.* Epidemiologic Methods.
2014;3(1):33–72.  
**[DOI: 10.1515/em-2013-0005](https://doi.org/10.1515/em-2013-0005)**

```text
                    CONTEXTUAL VARIATION
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       ▼
        SAME DIRECTION            DIRECTION CHANGES
        different magnitude       across context
                │                       │
                ▼                       ▼
          QUANTITATIVE             QUALITATIVE /
          INTERACTION               CROSSOVER
```

---

## 3.1 Quantitative Interaction: Same Direction, Different Magnitude

A **quantitative interaction** occurs when the relationship of a focal factor
with the outcome remains in the same direction across levels of another
factor, but its magnitude differs.

Using the notation developed above, suppose the relationship associated with
\(r\) is examined within \(c\) and \(\bar c\).

On the probability-difference scale:

```math
PD_{r\mid c}
=
p_{y\mid rc}
-
p_{y\mid\bar r c}
```

and

```math
PD_{r\mid\bar c}
=
p_{y\mid r\bar c}
-
p_{y\mid\bar r\bar c}.
```

A quantitative interaction can occur when, for example,

```math
PD_{r\mid c}>0
\qquad\text{and}\qquad
PD_{r\mid\bar c}>0,
```

but

```math
PD_{r\mid c}
\neq
PD_{r\mid\bar c}.
```

Thus, the **direction is retained**, but the **magnitude changes**.

```text
                    RELATIONSHIP OF r WITH y

c̄                  ───────────────►
                       positive

c                   ───────────────────────────►
                              positive

                    same direction
                    different magnitude
                           │
                           ▼
                 QUANTITATIVE INTERACTION
```

The same principle applies when both relationships are negative:

```math
PD_{r\mid c}<0
\qquad\text{and}\qquad
PD_{r\mid\bar c}<0,
```

while their magnitudes differ.

Therefore, quantitative interaction does **not** require a reversal of the
relationship. Context can modify how strongly a relationship is observed
while its direction remains unchanged.

### Game-research interpretation

Suppose:

```text
r = Ads
c = Game genre
y = Install success
```

Ads may be positively associated with install success in two genres while the
magnitude of that association differs substantially between them.

```text
Genre A       Ads ─────────► Install success
                    +0.08

Genre B       Ads ───────────────────► Install success
                              +0.25
```

Both relationships point in the same direction, but they are not equivalent
in magnitude.

The substantive conclusion is therefore not that Ads are associated with
success in one genre and failure in another. Rather, the **strength of the
observed Ads–success relationship depends on gameplay context**.

This distinction is particularly important for contextual analysis because an
overall relationship may conceal substantial variation in magnitude even when
its direction appears stable across contexts.

---

### Quantitative interaction is not the same as positive interaction

The word **quantitative** should not be confused with the sign of the
interaction measure.

For example, suppose:

```math
PD_{r\mid\bar c}=0.25
```

and

```math
PD_{r\mid c}=0.10.
```

Both relationships remain positive, so their directions agree. However,

```math
\mathrm{DDP}
=
0.10-0.25
=
-0.15.
```

Thus:

```text
Both stratum-specific relationships are positive
                    │
                    ▼
        Same direction across context
                    │
                    ▼
          QUANTITATIVE INTERACTION

BUT

Relationship is weaker within c
                    │
                    ▼
              DDP = -0.15
                    │
                    ▼
      NEGATIVE DEPARTURE FROM ADDITIVITY
```

This distinction is fundamental:

> **The direction of the interaction measure is not the same thing as the
> direction of the underlying stratum-specific relationships.**

A negative DDP can therefore arise even when the focal relationship remains
positive in both contexts, just as a positive DDP can arise when two negative
relationships differ in magnitude.

The sign of DDP describes the **direction of departure from the additive
reference**, whereas the signs of the stratum-specific probability
differences describe the **direction of the underlying relationships**.

## 3.2 Qualitative / Crossover Interaction

A stronger form of contextual variation occurs when the relationship between
\(r\) and \(y\) **changes direction across levels of \(c\)**.

This is commonly described as **qualitative interaction** or **crossover
interaction**.

Where quantitative interaction preserves the direction of the relationship,
qualitative interaction does not.

```text
                    RELATIONSHIP OF r WITH y
                              │
               ┌──────────────┴──────────────┐
               │                             │
               ▼                             ▼
       QUANTITATIVE                    QUALITATIVE /
        INTERACTION                      CROSSOVER
               │                             │
      direction retained              direction changes
      magnitude changes                across context
```

**Methodological source:**  
VanderWeele TJ, Knol MJ. *A Tutorial on Interaction.* Epidemiologic Methods.
2014;3(1):33–72.  
**[DOI: 10.1515/em-2013-0005](https://doi.org/10.1515/em-2013-0005)**

---

### Direction reversal across context

Using the probability-difference formulation developed above, consider the
relationship associated with \(r\) within \(c\):

```math
PD_{r\mid c}
=
p_{y\mid rc}
-
p_{y\mid\bar r c}
```

and within \(\bar c\):

```math
PD_{r\mid\bar c}
=
p_{y\mid r\bar c}
-
p_{y\mid\bar r\bar c}.
```

A qualitative interaction occurs when these relationships have **opposite
directions**.

For example:

```math
PD_{r\mid\bar c}>0
\qquad\text{and}\qquad
PD_{r\mid c}<0.
```

or conversely:

```math
PD_{r\mid\bar c}<0
\qquad\text{and}\qquad
PD_{r\mid c}>0.
```

The important feature is therefore the sign reversal:

```math
\boxed{
PD_{r\mid c}\times PD_{r\mid\bar c}<0
}
```

Conceptually:

```text
c̄                    r̄ ─────────────► r
                         positive
                            │
                            │ context changes
                            ▼
c                     r̄ ◄───────────── r
                         negative

                            │
                            ▼
                   DIRECTION REVERSAL
                            │
                            ▼
                QUALITATIVE / CROSSOVER
                     INTERACTION
```

The relationship associated with \(r\) is therefore not adequately described
by saying that it merely becomes stronger or weaker. Its **direction depends
on the contextual condition**.

---

### A simple numerical example

Suppose:

```math
p_{y\mid\bar r\bar c}=0.30,
\qquad
p_{y\mid r\bar c}=0.50.
```

When \(c\) is absent:

```math
PD_{r\mid\bar c}
=
0.50-0.30
=
+0.20.
```

Now suppose:

```math
p_{y\mid\bar r c}=0.60,
\qquad
p_{y\mid rc}=0.40.
```

When \(c\) is present:

```math
PD_{r\mid c}
=
0.40-0.60
=
-0.20.
```

Thus:

```text
c̄             0.30 ─────────────► 0.50
                         +0.20

c              0.60 ◄───────────── 0.40
                         -0.20

                         │
                         ▼
                 relationship reverses
                         │
                         ▼
               CROSSOVER INTERACTION
```

The additive interaction contrast is:

```math
\mathrm{DDP}
=
(-0.20)-(+0.20)
=
-0.40.
```

The DDP captures the difference between the two stratum-specific probability
differences, while the **crossover classification** comes from the fact that
those relationships have opposite signs.

---

### Why crossover is different from a large interaction contrast

A large DDP or RoR does not, by itself, establish crossover interaction.

Consider:

```math
PD_{r\mid\bar c}=+0.10
```

and

```math
PD_{r\mid c}=+0.40.
```

The relationship changes substantially in magnitude, but both values remain
positive.

```text
+0.10 ─────────────► +0.40

same direction
different magnitude

QUANTITATIVE INTERACTION
```

By contrast:

```math
PD_{r\mid\bar c}=+0.10
```

and

```math
PD_{r\mid c}=-0.10
```

cross the null value:

```text
+0.10 ───────► 0 ◄─────── -0.10

      direction changes

QUALITATIVE / CROSSOVER INTERACTION
```

Thus, **magnitude of departure** and **direction reversal** describe different
features of the contextual pattern.

---

### Visual signature of crossover

Crossover interaction is particularly intuitive when represented using
stratum-specific probability profiles.

```text
Probability
of success

high │       ╲        ╱
     │        ╲      ╱
     │         ╲    ╱
     │          ╲  ╱
     │           ╳
     │          ╱ ╲
     │         ╱   ╲
low  │        ╱     ╲
     └────────────────────
             c̄      c
```

The crossing lines indicate that the ordering of the groups changes across
context.

However, the visual crossing should be interpreted together with the
underlying estimates and their uncertainty rather than treated as sufficient
statistical evidence by itself.

---

### Translation to game research

Consider a gameplay example in which:

```text
r = Game type
c = Age-rating context
y = Marketplace success
```

Suppose one game type is associated with a higher probability of marketplace
success under a broad age-rating condition, but with a lower probability under
a restrictive age-rating condition.

```text
                         Broad rating       Restrictive rating

Game type A                  HIGH  ───────────────╲  LOW
                                                  ╲
                                                   ╳
                                                  ╱
Game type B                  LOW   ──────────────╱   HIGH
```

The contextual condition does more than alter the magnitude of the observed
relationship. It changes its direction.

The appropriate interpretation is therefore:

> **The direction of the observed game-type–marketplace-success relationship
> differs across the age-rating context represented in the data.**

For observational marketplace data, this is a statement about **conditional
empirical relationships**. It does not, by itself, establish that the
contextual variable causally produces the reversal.

---

### Quantitative versus qualitative interaction

The distinction can now be summarized as:

| Pattern | Relationship within c̄ | Relationship within c | Defining feature |
|---|---:|---:|---|
| **No contextual variation** | + | + | Same direction and equivalent magnitude |
| **Quantitative interaction** | + | + | Same direction, different magnitude |
| **Quantitative interaction** | − | − | Same direction, different magnitude |
| **Qualitative / crossover interaction** | + | − | Direction reversal |
| **Qualitative / crossover interaction** | − | + | Direction reversal |

The same distinction can be expressed visually:

```text
QUANTITATIVE                       QUALITATIVE / CROSSOVER

c̄   ─────────►                    c̄   ─────────►
c    ─────────────────►            c    ◄─────────

same direction                     opposite directions
different magnitude                direction reversal
```

Qualitative interaction therefore represents a particularly consequential
form of contextual dependence because a single overall direction can fail to
represent the relationships observed within different contexts.

## 3.3 Amplification and Attenuation

When a relationship retains the same direction across contexts, contextual
variation can often be described in terms of **amplification** or
**attenuation**.

These terms describe what happens to the **magnitude of the underlying
relationship** as the contextual condition changes.

```text
                 SAME-DIRECTION RELATIONSHIP
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       ▼
         magnitude becomes       magnitude becomes
              larger                  smaller
                │                       │
                ▼                       ▼
          AMPLIFICATION             ATTENUATION
```

This distinction belongs within the broader category of **quantitative
interaction** introduced above: the direction is retained, but the strength
of the relationship differs across context.

---

### Amplification

Amplification occurs when the magnitude of the relationship between \(r\)
and \(y\) is greater within one contextual condition than within the
reference condition.

For a positive probability-difference relationship, suppose:

```math
PD_{r\mid\bar c}=+0.10
```

and

```math
PD_{r\mid c}=+0.30.
```

The relationship remains positive, but becomes stronger in the presence of
\(c\):

```text
c̄        r̄ ─────────► r
              +0.10

c         r̄ ─────────────────────► r
                       +0.30

                  same direction
                        +
                 larger magnitude
                        │
                        ▼
                  AMPLIFICATION
```

The corresponding additive interaction contrast is:

```math
\mathrm{DDP}
=
0.30-0.10
=
+0.20.
```

Here, the positive DDP and amplification point in the same direction because
the underlying relationship is positive and becomes more positive within
\(c\).

---

### Attenuation

Now suppose:

```math
PD_{r\mid\bar c}=+0.30
```

but

```math
PD_{r\mid c}=+0.10.
```

The relationship remains positive, but its magnitude becomes smaller:

```text
c̄        r̄ ─────────────────────► r
                       +0.30

c         r̄ ─────────► r
              +0.10

                  same direction
                        +
                 smaller magnitude
                        │
                        ▼
                   ATTENUATION
```

The DDP is:

```math
\mathrm{DDP}
=
0.10-0.30
=
-0.20.
```

Thus, in this example, the negative departure corresponds to attenuation of
an underlying positive relationship.

---

### Why the sign of DDP is not sufficient

Amplification and attenuation should **not be assigned solely from whether
DDP is positive or negative**.

Consider an underlying negative relationship.

Suppose:

```math
PD_{r\mid\bar c}=-0.10
```

and

```math
PD_{r\mid c}=-0.30.
```

The relationship becomes **more strongly negative** within \(c\).

Its magnitude changes from

```math
|{-0.10}|=0.10
```

to

```math
|{-0.30}|=0.30.
```

Therefore, the relationship has been **amplified in magnitude**.

Yet:

```math
\mathrm{DDP}
=
-0.30-(-0.10)
=
-0.20.
```

So a negative DDP can describe amplification when the underlying relationship
is negative.

Conversely:

```math
PD_{r\mid\bar c}=-0.30
```

and

```math
PD_{r\mid c}=-0.10
```

represent attenuation of the negative relationship, even though:

```math
\mathrm{DDP}
=
-0.10-(-0.30)
=
+0.20.
```

The distinction is therefore:

```text
SIGN OF DDP
     │
     ▼
Direction of departure from
the additive reference


AMPLIFICATION / ATTENUATION
     │
     ▼
Change in magnitude of the
underlying relationship
```

These are related descriptions, but they are **not interchangeable**.

---

### A magnitude-based representation

For same-direction relationships, amplification can be represented
descriptively as:

```math
\left|PD_{r\mid c}\right|
>
\left|PD_{r\mid\bar c}\right|,
```

whereas attenuation corresponds to:

```math
\left|PD_{r\mid c}\right|
<
\left|PD_{r\mid\bar c}\right|.
```

This absolute-magnitude comparison is useful for describing the pattern, but
it should not replace DDP as the formal additive interaction contrast.

```text
                       FORMAL CONTRAST
                             │
                             ▼
                            DDP
                             │
                  direction of departure


                    PATTERN DESCRIPTION
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
       |relationship| grows          |relationship| shrinks
              │                             │
              ▼                             ▼
       AMPLIFICATION                  ATTENUATION
```

---

### Multiplicative interpretation

The same conceptual distinction can be made on the odds-ratio scale, but the
null reference is now \(1\), rather than \(0\).

For example:

```math
\theta_{yr\mid\bar c}=1.20
```

and

```math
\theta_{yr\mid c}=1.80
```

describe a positive association that is stronger within \(c\).

The corresponding ratio of odds ratios is:

```math
\mathrm{RoR}
=
\frac{1.80}{1.20}
=
1.50.
```

However, as with DDP, the value of RoR must be interpreted together with the
underlying conditional odds ratios.

For example:

```math
\theta_{yr\mid\bar c}=0.80,
\qquad
\theta_{yr\mid c}=0.50
```

describes an association moving farther below the null value of \(1\), even
though:

```math
\mathrm{RoR}
=
\frac{0.50}{0.80}
=
0.625.
```

Therefore, RoR describes the **relative change between conditional odds
ratios**, whereas amplification or attenuation describes how the magnitude of
the underlying association changes relative to its null.

---

### Translation to game research

Suppose:

```text
r = Free
c = Offers IAP
y = Marketplace success
```

The relationship between being Free and marketplace success can first be
estimated among games without IAP and then among games offering IAP.

Conceptually:

```text
                       FREE–SUCCESS
                       RELATIONSHIP
                            │
                 compare across IAP
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
           No IAP                        IAP
              │                           │
       weaker relationship        stronger relationship
              │                           │
              └─────────────┬─────────────┘
                            ▼
                    AMPLIFICATION
```

If the Free–success relationship remains in the same direction but becomes
substantially stronger among games offering IAP, the observed pattern can be
described as **amplification of the Free–success relationship in the IAP
context**.

The reverse pattern—where the relationship remains in the same direction but
moves closer to its null—can be described as **attenuation**.

Because these are observational marketplace relationships, amplification and
attenuation here describe changes in the **observed conditional association**;
they do not imply that the contextual factor causally strengthens or weakens
the relationship.

---

### Relationship to the preceding concepts

The terminology can now be organized as:

```text
                    CONTEXTUAL VARIATION
                            │
             Does direction change?
                            │
                ┌───────────┴───────────┐
                │                       │
               NO                      YES
                │                       │
                ▼                       ▼
         QUANTITATIVE              QUALITATIVE /
          INTERACTION                CROSSOVER
                │
        Does magnitude change?
                │
       ┌────────┴────────┐
       ▼                 ▼
   becomes             becomes
   stronger             weaker
       │                 │
       ▼                 ▼
AMPLIFICATION        ATTENUATION
```

Thus, **quantitative interaction** identifies a same-direction difference in
magnitude, while **amplification** and **attenuation** provide descriptive
language for the direction of that magnitude change.

The next distinction concerns patterns in which additive and multiplicative
interaction do not agree, showing why the same contextual relationship may
appear differently depending on the scale used to evaluate it.

## References

1. Knol MJ, VanderWeele TJ. Recommendations for presenting analyses of effect modification and interaction. *International Journal of Epidemiology*. 2012;41(2):514–520.  
   **[https://doi.org/10.1093/ije/dyr218](https://doi.org/10.1093/ije/dyr218)**

2. Greenland S. Tests for interaction in epidemiologic studies: A review and a study of power. *Statistics in Medicine*. 1983;2(2):243–251.  
   **[https://doi.org/10.1002/sim.4780020219](https://doi.org/10.1002/sim.4780020219)**

3. Greenland S. Effect Modification and Interaction. *Wiley StatsRef: Statistics Reference Online*.  
   **[https://doi.org/10.1002/9781118445112.stat03728.pub2](https://doi.org/10.1002/9781118445112.stat03728.pub2)**

4. Brumback BA. On effect-measure modification: Relationships among changes in the relative risk, odds ratio, and risk difference. *Statistics in Medicine*. 2008;27(18):3453–3465.  
   **[https://doi.org/10.1002/sim.3246](https://doi.org/10.1002/sim.3246)**

5. VanderWeele TJ, Knol MJ. A Tutorial on Interaction. *Epidemiologic Methods*. 2014;3(1):33–72.  
   **[https://doi.org/10.1515/em-2013-0005](https://doi.org/10.1515/em-2013-0005)**

6. Andersson T, Alfredsson L, Källberg H, Zdravkovic S, Ahlbom A. Calculating measures of biological interaction. *European Journal of Epidemiology*. 2005;20(7):575–579.  
   **[https://doi.org/10.1007/s10654-005-7835-x](https://doi.org/10.1007/s10654-005-7835-x)**

7. Richardson DB, Kaufman JS. Estimation of the Relative Excess Risk Due to Interaction and Associated Confidence Bounds. *American Journal of Epidemiology*. 2009;169(6):756–760.  
   **[https://doi.org/10.1093/aje/kwn411](https://doi.org/10.1093/aje/kwn411)**

8. Knol MJ, VanderWeele TJ, Groenwold RHH, Klungel OH, Rovers MM, Grobbee DE. Estimating measures of interaction on an additive scale for preventive exposures. *European Journal of Epidemiology*. 2011;26:433–438.  
   **[https://doi.org/10.1007/s10654-011-9554-9](https://doi.org/10.1007/s10654-011-9554-9)**
