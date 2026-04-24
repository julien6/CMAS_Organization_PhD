# NeurIPS 2026 Refactor Roadmap and Traceability

This file is the working control document for the NeurIPS refactor. The paper
now follows this argument:

Problem -> General objective -> Sub-objectives -> Theoretical gaps -> Single
contribution (NS-MAWM) -> Claims -> Deductive/inductive validation -> Evidence
-> Limitations.

## Completion Snapshot

| Phase | Status | Output |
| --- | --- | --- |
| P0. Audit current paper | Completed draft | JFSMA and ICML review issues consolidated. Main unresolved items now depend on final experiments, mask audit, dependency export, and bibliography cleanup. |
| P1. Scientific framing | Completed draft | Problem, objective, sub-objectives, three theoretical gaps, single-contribution framing integrated in `article.tex`. |
| P2. Claims and proof strategy | Completed draft | Claims paragraph and formal covered-feature validity proposition integrated in `article.tex`. |
| P3. Related work rewrite | In progress | Related work derives three theoretical gaps through sub-objective criteria. Main remaining work: sharpen citations and reduce comparison-table ambiguity. |
| P4. Formalization/method cleanup | Completed draft | Problem formulation, notation table, "symbolically predictable/covered" terminology, coverage ratio, RVR_pre/post, correction magnitude, covered-feature validity, covered/residual error decomposition, cleaned method figure, and algorithmic pseudocode added. |
| P5. Experimental setup rewrite | Completed draft | Validation matrix, claim-evidence registry, downstream planning/control protocol, rule coverage scaffold, baseline table, and result-family scaffolds added. |
| P6. Final result integration | In progress | Aggregate table and final-ready scaffolds exist for prediction, semantic drift, rule dropout, planning/OOD, and data-limited learning. Needs real final aggregates, error bars, statistical analysis, and finalized plots. |
| P7. NeurIPS compliance | In progress | Checklist filled, authors anonymized, acknowledgements removed, appendix scaffolds added, ICML/JFSMA action plans and NeurIPS readiness audit created, section titles/style normalized, internal pending checklist removed from article, one malformed BibTeX entry fixed, asset/license and dependency tables added. Final licenses, exact compute, and final archive synchronization remain. |

Estimated global completion after the current pass: about 72%.

## General Problem

Multi-agent world models are expected to support planning and control through
imagined rollouts. In partially observable multi-agent environments, useful
rollouts must be numerically accurate and semantically reliable: they should
preserve spatial, logical, and interaction constraints over time, even when
available symbolic knowledge is partial.

## General Objective

Develop semantically reliable multi-agent world models by integrating partial
symbolic transition knowledge into learned neural dynamics.

## Sub-Objectives

| ID | Sub-objective |
| --- | --- |
| SO1 | Expose the semantic structure of multi-agent observations. |
| SO2 | Separate symbolically predictable dynamics from residual uncertainty. |
| SO3 | Couple partial symbolic transition knowledge with neural prediction. |
| SO4 | Preserve semantic validity over long rollouts. |
| SO5 | Make rollouts useful for downstream model-based decision making. |
| SO6 | Remain effective when symbolic knowledge is partial. |

## Theoretical Gaps

| ID | Gap | Derived from |
| --- | --- | --- |
| G1 | Semantic formalization gap: existing multi-agent WMs lack a dedicated structure for representing which components of partially observable joint observations are symbolically coverable and which remain residual. | SO1, SO2 |
| G2 | Neuro-symbolic dynamics integration gap: existing approaches lack unified mechanisms for coupling partial symbolic transition knowledge with neural multi-agent WM dynamics once such a semantic structure is available. | SO3 |
| G3 | Neuro-symbolic impact evaluation gap: existing work lacks a systematic framework for evaluating whether neuro-symbolic integration improves long-horizon semantic reliability, downstream decision quality, data efficiency, OOD behavior, and robustness as symbolic coverage varies. | SO4, SO5, SO6 |

## Single Contribution

The paper proposes NS-MAWM, a neuro-symbolic framework for semantically reliable
multi-agent world models. NS-MAWM is the single scientific contribution.

Facets of NS-MAWM:

- structured feature decomposition into covered and residual components;
- partial symbolic transition operator;
- coverage mask and coverage ratio;
- three coupling modes: regularization, projection, residual dynamics;
- semantic coherence evaluation through RVR_pre, RVR_post, and correction magnitude.

Protocols, code, hyperparameters, compute reporting, and rule inventories are
validation/reproducibility apparatus, not independent contributions.

## Claims and Validation Strategy

| Claim | Gap | Deductive support | Inductive evidence |
| --- | --- | --- | --- |
| C1. Hybrid semantic representation | G1 | Formal decomposition `F = F_d union F_u` and covered/residual prediction. | Prediction and ablations comparing residual vs monolithic neural WMs. |
| C2. Unified symbolic coupling | G2 | Regularization, projection, and residual dynamics derive from `(T_theta, T_s, M_d)`. | Empirical comparison across integration modes. |
| C3. Covered-feature semantic validity | G2, G3 | If rules and masks are correct, projection/residual yield `RVR_post = 0` on `F_d`. | RVR_pre/post and correction magnitude. |
| C4. Reduced long-horizon semantic drift | G3 | Conditional guarantee only on covered features under repeated hard enforcement. | MSE_H, RVR_H, invalid transition rate, degradation slope. |
| C5. Improved downstream utility | G3 | Conditional model-error/value-error reasoning; no universal guarantee. | Return, success rate, invalid plan rate under planning/control. |
| C6. Partial-knowledge robustness | G3 | Guarantees scale only with coverage ratio `kappa`; uncovered features remain neural. | Rule dropout and OOD generalization experiments. |
| C7. Data-limited learning benefit | G3 | No deductive guarantee; symbolic structure may reduce neural sample burden. | Replay-subset experiments comparing gains at `N_small`, `N_med`, and `N_full`. |

## Immediate Next Tasks

1. Replace all provisional result values and narrative percentages with final experimental aggregates.
2. Compute and insert real rule coverage ratios `kappa` for every environment.
3. Add final per-environment plots or tables for horizon drift, rule dropout, OOD generalization, and planning/control.
4. Clean `references.bib` globally: verify venues, versions, URLs, licenses, and remove unused or weak references.
5. Fill exact compute resources, wall-clock time, and dependency/license versions in the appendix and checklist.
6. Perform a final anonymity pass over source, bibliography keys, comments, URLs, and supplemental material.
7. Synchronize the anonymous code archive with all commands, configs, seeds, and result tables.
8. Deferred by decision: reduce the main text to the NeurIPS page budget and resolve remaining layout warnings.

## Review-Response Coverage

| Review source | Main issues now structurally addressed | Still pending final evidence |
| --- | --- | --- |
| ICML EPKz | determinable terminology removed; rules distinguished from reward engineering; RVR_pre/RVR_post and broader impacts added. | rule-authoring effort should be quantified after final rule inventory. |
| ICML qGB8 | downstream planning/control axis added; notation table and Dec-POMDP definitions cleaned; rule coverage scaffold added. | final downstream results and exact coverage ratios. |
| ICML YgDJ | claim-evidence registry, result scaffolds, implementation details, and RVR comparability language added. | final quantitative tables for all announced axes. |
| ICML Nx4Y | covered-feature validity proposition, covered/residual error decomposition, baseline/ablation table, and SMACv2 terminology added. | final statistical tests, additional ablations, and downstream results. |
| JFSMA R1-R3 | post-correction scope clarified; PINN/constrained-learning analogy added; reproducibility/checklist scaffolds added; limitations strengthened. | bibliography audit, exact dependencies, exact compute, final code archive synchronization. |
