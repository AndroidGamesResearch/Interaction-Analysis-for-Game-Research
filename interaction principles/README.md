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

- \(A\) = first factor
- \(B\) = second factor
- \(Y\) = outcome

For two binary factors, four joint conditions are possible:

| | \(B=0\) | \(B=1\) |
|---|---:|---:|
| **\(A=0\)** | \(P_{00}\) | \(P_{01}\) |
| **\(A=1\)** | \(P_{10}\) | \(P_{11}\) |

where

```math
P_{ab}=P(Y=1\mid A=a,B=b).
```

Thus,

```math
P_{00}=P(Y=1\mid A=0,B=0)
```

is the outcome probability when neither factor is present, whereas

```math
P_{11}=P(Y=1\mid A=1,B=1)
```

is the outcome probability when both factors are present.

These four conditions provide the basic structure from which interaction can be evaluated.

### What makes it an interaction?

A large value of \(P_{11}\) is **not, by itself, evidence of interaction**.

The critical question is whether the observed joint relationship differs from the relationship expected from the separate relationships of \(A\) and \(B\) under a specified **no-interaction model**.

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

On the probability-difference scale, the individual relationships associated with \(A\) and \(B\) can be written as

```math
PD_A=P_{10}-P_{00}
```

and

```math
PD_B=P_{01}-P_{00}.
```

Under an additive no-interaction model, the expected joint probability is

```math
P_{11}^{(\mathrm{expected})}
=
P_{10}+P_{01}-P_{00}.
```

The departure from additivity is therefore

```math
IC_{\mathrm{add}}
=
P_{11}-P_{10}-P_{01}+P_{00}.
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
RR_{10}=\frac{P_{10}}{P_{00}},
\qquad
RR_{01}=\frac{P_{01}}{P_{00}},
\qquad
RR_{11}=\frac{P_{11}}{P_{00}}.
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
                    P₀₀ P₁₀ P₀₁ P₁₁
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

The same structure can be used when \(A\) and \(B\) represent characteristics of games rather than epidemiological exposures.

For example:

```text
A = Free
B = Offers IAP
Y = Marketplace success
```

This gives four conditions:

| | No IAP | IAP |
|---|---:|---:|
| **Not Free** | \(P_{00}\) | \(P_{01}\) |
| **Free** | \(P_{10}\) | \(P_{11}\) |

The interaction question is **not simply whether Free + IAP games have high marketplace success**.

Instead, the question is:

> **Is the joint Free × IAP relationship with marketplace success different from what would be expected from the separate Free and IAP relationships under the specified interaction scale?**

This distinction becomes important when specific interaction patterns are introduced later on this page.

---

## 1.2 Effect Modification

Interaction can focus on the joint relationship of two factors. **Effect modification changes the orientation of the question.**

Suppose:

- \(A\) = focal factor
- \(X\) = modifying factor
- \(Y\) = outcome

Instead of primarily evaluating the joint \(A \times X\) relationship, the relationship between \(A\) and \(Y\) is examined within different levels of \(X\):

```math
M(A,Y\mid X=0)
```

versus

```math
M(A,Y\mid X=1).
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

If the relationship differs across levels of \(X\), the \(A\)–\(Y\) relationship is modified across \(X\).

The conceptual distinction can therefore be expressed as:

```text
INTERACTION

"What happens when A and B occur jointly?"

                    versus

EFFECT MODIFICATION

"Does the A–Y relationship differ across levels of X?"
```

**Methodological source:**  
Knol MJ, VanderWeele TJ. *Recommendations for presenting analyses of effect modification and interaction.* International Journal of Epidemiology. 2012;41(2):514–520.  
**[DOI: 10.1093/ije/dyr218](https://doi.org/10.1093/ije/dyr218)**

---

### Translation to game research

Let:

```text
A = Ads
X = Game genre
Y = Marketplace success
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

Let \(M\) denote a chosen measure of the \(A\)–\(Y\) relationship.

Effect-measure modification can be represented as

```math
M(A,Y\mid X=0)
\neq
M(A,Y\mid X=1).
```

More generally, across \(K\) contexts:

```math
M(A,Y\mid X=1),\;
M(A,Y\mid X=2),\;
\dots,\;
M(A,Y\mid X=K)
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
       M_add(A,Y|X)          M_mult(A,Y|X)
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
│  Do A and B jointly depart from the relationship expected   │
│  from their separate relationships on a specified scale?    │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                    EFFECT MODIFICATION                       │
│                                                              │
│  Does the relationship between A and Y differ across        │
│  levels of X?                                               │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                EFFECT-MEASURE MODIFICATION                   │
│                                                              │
│  Does a specified measure of the A–Y relationship differ    │
│  across levels of X?                                        │
└──────────────────────────────────────────────────────────────┘
```

These concepts provide the foundation for the interaction principles developed in the following sections.

The next step is to distinguish **additive and multiplicative interaction**, define the corresponding **no-interaction reference on each scale**, and examine how departures from those references can be interpreted.

---

## References

1. Knol MJ, VanderWeele TJ. Recommendations for presenting analyses of effect modification and interaction. *International Journal of Epidemiology*. 2012;41(2):514–520.  
   **[https://doi.org/10.1093/ije/dyr218](https://doi.org/10.1093/ije/dyr218)**

2. Greenland S. Tests for interaction in epidemiologic studies: A review and a study of power. *Statistics in Medicine*. 1983;2(2):243–251.  
   **[https://doi.org/10.1002/sim.4780020219](https://doi.org/10.1002/sim.4780020219)**

3. Greenland S. Effect Modification and Interaction. *Wiley StatsRef: Statistics Reference Online*.  
   **[https://doi.org/10.1002/9781118445112.stat03728.pub2](https://doi.org/10.1002/9781118445112.stat03728.pub2)**

4. Brumback BA. On effect-measure modification: Relationships among changes in the relative risk, odds ratio, and risk difference. *Statistics in Medicine*. 2008;27(18):3453–3465.  
   **[https://doi.org/10.1002/sim.3246](https://doi.org/10.1002/sim.3246)**
