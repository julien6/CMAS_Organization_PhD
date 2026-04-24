# ICML Reviews: Organized Critique and NeurIPS Action Plan

This document consolidates the actionable feedback from the ICML 2026 reviews
and maps it to the NeurIPS refactor. It complements the JFSMA action plan:
JFSMA was strongest on notation, bibliography, and reproducibility, while ICML
was strongest on claim support, downstream validation, metric interpretation,
and theoretical analysis.

## 0. Reviewer-Level Summary

### EPKz: weak accept, mostly clarity and impact framing

Main concerns:

- Rule specification may create a domain-engineering burden similar to reward
  design.
- The term "determinable" is ambiguous.
- RVR should be interpreted carefully because hard symbolic modes can make
  violations disappear by construction.
- Broader impacts should discuss positive and negative consequences of semantic
  reliability in high-stakes domains.

Current NeurIPS status:

- "Determinable" has been replaced by "symbolically predictable" or "covered".
- RVR is split into RVR_pre and RVR_post, with correction magnitude.
- Broader impacts now discuss auditability and misplaced trust.
- Remaining improvement: make the rule-design burden versus reward-engineering
  distinction explicit in the paper.

### qGB8: weak reject, insufficient downstream evaluation and notation

Main concerns:

- Abstract/introduction claim planning and control improvements, but the ICML
  version mostly reported prediction metrics.
- Handcrafted symbolic rules raise scalability and adaptation concerns.
- Some notation, including Omega and action spaces, was undefined.

Current NeurIPS status:

- Downstream planning/control is now a required validation axis with a dedicated
  protocol and result scaffold.
- Rule coverage and partial rule dropout are now explicit.
- Core notation table and Dec-POMDP definitions have been added.
- Remaining improvement: final downstream results must be inserted; exact rule
  coverage ratios must be computed from masks.

### YgDJ: reject, weak simulation/results and poor metric interpretation

Main concerns:

- Evaluation promised prediction, symbolic coherence, downstream control, and
  generalization, but only MSE_H and RVR were shown.
- RVR is not fully convincing across methods because hard projection/residual
  modes make RVR_post zero by construction.
- Implementation details, environment/task specifications, symbolic rules, and
  feature coverage are insufficient.
- It is unclear whether zero RVR is an empirical achievement or a deterministic
  consequence of output overwriting.

Current NeurIPS status:

- Claim-evidence registry added.
- Result scaffolds added for semantic drift, rule dropout, OOD, downstream
  planning/control, and data-limited learning.
- RVR_pre/RVR_post/correction magnitude separate learned coherence from enforced
  coherence.
- Rule coverage table scaffold added.
- Remaining improvement: fill final numerical results and rule coverage ratios.

### Nx4Y: reject, theory and experiments insufficient

Main concerns:

- Theoretical analysis is weak: no proof that symbolic constraints reduce drift,
  no convergence/error bounds, no statistical analysis of RVR.
- Baselines and ablations are inadequate.
- Downstream tasks are not analyzed.
- Minor: SMAC should be SMACv2.

Current NeurIPS status:

- A conditional covered-feature validity proposition has been added.
- The paper explicitly avoids claiming universal drift or return guarantees.
- Baseline/ablation roles now include neural, neural+post-correction,
  regularization, projection, residual, and oracle covered-feature diagnostics.
- Downstream planning/control scaffold added.
- SMACv2 terminology is being normalized.
- Remaining improvement: add RVR as an empirical violation-probability
  estimator; add a covered/residual error decomposition; insert final downstream
  and ablation numbers.

## 1. Cross-Review Critical Issues

### 1.1 Claim-evidence mismatch

Required NeurIPS action:

- Every abstract/introduction claim must map to a table, figure, proposition, or
  limitation.
- Planning/control, generalization, robustness, and sample efficiency must
  either have results or be clearly identified as target validation axes pending
  final synchronization.

Status: structurally addressed; final values pending.

### 1.2 RVR comparability

Required NeurIPS action:

- Never present zero RVR_post for projection/residual as learned empirical
  superiority.
- Report RVR_pre for learned coherence, RVR_post for final rollout validity, and
  correction magnitude for the size of symbolic intervention.
- Define RVR statistically as an empirical violation probability over covered
  agent-feature-time triples.

Status: mostly addressed; statistical definition strengthened in the next pass.

### 1.3 Theoretical analysis

Required NeurIPS action:

- State the exact conditional guarantee on covered features.
- Add a covered/residual error decomposition showing what symbolic rules can and
  cannot guarantee.
- Explicitly state that no universal convergence or downstream-return guarantee
  is claimed.

Status: partly addressed; decomposition strengthened in the next pass.

### 1.4 Rule specification burden

Required NeurIPS action:

- Explain why symbolic transition rules differ from reward shaping:
  rewards define desired behavior, while rules encode plausible transitions.
- Still acknowledge that both introduce domain-engineering risk.
- Add rule dropout and coverage reporting as mitigations, not as complete
  solutions.

Status: partly addressed; explicit paragraph added in the next pass.

### 1.5 Reproducibility and implementation detail

Required NeurIPS action:

- Provide pseudocode/commands/config mapping.
- Report hyperparameters, environment specs, versions, rule inventories, masks,
  coverage ratios, and seeds.
- Address Overcooked/Gym/Gymnasium/NumPy compatibility.

Status: scaffold added; final versions/logs pending.

## 2. Remaining High-Priority NeurIPS Work

1. Insert final downstream planning/control results.
2. Insert final OOD, rule-dropout, and data-limited results.
3. Compute real coverage ratios kappa from rule masks.
4. Replace all placeholder numerical scaffolds with final script outputs.
5. Add final statistical tests/effect sizes over matched seeds.
6. Pin exact dependency versions and add smoke tests in the archive.
7. Complete bibliography audit.
8. Compress to NeurIPS page limit after scientific content is stable.

