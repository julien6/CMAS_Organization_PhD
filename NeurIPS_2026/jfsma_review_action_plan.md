# JFSMA Reviews: Organized Critique and NeurIPS Action Plan

This document consolidates all actionable remarks from the JFSMA reviews for the
NS-MAWM paper. It is intentionally exhaustive: minor typographic comments are
kept because several of them point to recurring readability problems.

## 0. Reviewer-Level Summary

### R1: Positive, with two important scientific issues

Overall assessment: accepted as long paper. The reviewer finds the article well
written, well organized, thematically relevant to JFSMA, and novel in the
multi-agent learning context. The code/data release is explicitly praised.

Main concerns:

- The post-prediction symbolic correction mechanism is described but not used in
  the experiments.
- Several evaluations are announced but not actually shown: robustness,
  generalization, rule ablation, data frugality, standard errors, execution
  time.
- Manual rule design is acknowledged, but alternative perspectives such as
  domain ontologies could be discussed.
- The writing contains typos, punctuation problems, anglicisms, and unclear
  expressions.

### R2: Positive, but formalization and references need major cleanup

Overall assessment: accepted as long paper. The reviewer finds the contribution
important and clearly positioned, but considers the mathematical formalization
and bibliography insufficiently clean.

Main concerns:

- The references are described as "completely to review": incomplete authors,
  wrong first/last names, missing venues, missing capitalization, missing
  conference/journal information.
- The formalization contains inconsistent notation, undefined variables, index
  errors, dimension mismatches, unclear order of definitions, and overly long
  formulas.
- Some sections repeat content or introduce concepts in the wrong order.
- Figures and formulas are not sufficiently cited/explained in the surrounding
  text.
- The provided code has a reproducibility issue for Overcooked due to Gym being
  unmaintained and incompatible with NumPy 2.0; exact dependency versions should
  be fixed.
- Statistical uncertainty and significance are missing from the results.

### R3: Positive, with concerns about scope and generality

Overall assessment: accepted as long paper. The reviewer values the
neuro-symbolic contribution, especially for preventing absurd predictions in
structured multi-agent environments.

Main concerns:

- The approach remains partly opaque because neural residual dynamics are still
  learned in a latent space that is not deeply understood.
- Hand-written rules stabilize the model but may limit flexibility when the
  environment changes.
- The evaluation is convincing within structured environments, but its general
  scope remains limited.
- Computational cost, scalability with many agents/rules, and the triviality of
  RVR for projection/residual variants need clearer discussion.

## 1. Scientific Positioning and Claims

### 1.1 Clarify what is contribution and what is evaluation apparatus

Source reviewers: R1, R2, R3.

Problem:

- The paper can appear to present multiple contributions: three strategies,
  RVR, post-correction, code, experimental protocol, rule sets.
- R2 says the reader may not know whether some background sections are original
  contributions or state of the art.
- R3 sees RVR as useful but partially trivial for hard-symbolic variants.

Required NeurIPS action:

- State explicitly that NS-MAWM is the single contribution.
- Present regularization, projection, residual dynamics, RVR, rule inventories,
  protocols, and code as facets/evaluation apparatus of NS-MAWM, not separate
  contributions.
- Separate deductive guarantees from empirical claims.
- Explain that RVR is a diagnostic metric: RVR_post is a guarantee check for
  hard modes, while RVR_pre and correction magnitude are the comparative metrics
  for learned coherence.

Target sections:

- Abstract
- Introduction / contribution paragraph
- Method / formal properties
- Evaluation / metrics
- Limitations

Priority: high.

### 1.2 Strengthen the neuro-symbolic positioning

Source reviewers: R1, R2.

Problem:

- R2 notes a strong parallel with Physics-Informed Neural Networks (PINNs):
  constraints can be inserted as preprocessing, architecture, loss
  regularization, or post-processing.
- R1 suggests domain ontologies as an alternative to LLM-generated rules.

Required NeurIPS action:

- Add a paragraph in related work comparing NS-MAWM to constrained learning,
  PINNs, semantic loss, differentiable logic, and post-processing/projection
  methods.
- Explain what is new in the MARL setting: partial observability, joint
  observations, agent-indexed symbolic masks, long-horizon rollout drift, and
  downstream model-based decision making.
- Add ontologies/domain knowledge extraction as an alternative future direction
  to LLM-based rule generation.

Target sections:

- Related Work
- Limitations / Future Work

Priority: high.

### 1.3 Clarify scope and generality

Source reviewer: R3.

Problem:

- The evaluation environments are structured and favorable to symbolic rules.
- The approach may not generalize to rich real-world multi-agent systems with
  hidden variables, stochasticity, and incomplete rule coverage.

Required NeurIPS action:

- Explicitly define the intended scope: structured observations with partial
  symbolic regularities.
- State that NS-MAWM is not a complete model of open-ended multi-agent worlds.
- Add experiments or at least analysis for OOD configurations and rule dropout.
- Discuss failure modes when symbolic knowledge is wrong, sparse, or obsolete.

Target sections:

- Problem formulation
- Evaluation
- Limitations

Priority: high.

## 2. Experimental Evidence and Missing Results

### 2.1 Align announced evaluations with reported results

Source reviewers: R1, R2.

Problem:

- R1 says the article announces robustness/generalization, rule ablation,
  unknown configurations, data frugality, and post-correction, but does not show
  all corresponding results.
- R2 asks whether result interpretations are statistically significant.

Required NeurIPS action:

- For every claim in the abstract/introduction, add an explicit result table or
  state that the claim is not evaluated.
- Add a claim-to-evidence table.
- Add final result tables for:
  - long-horizon prediction,
  - semantic drift,
  - pre/post RVR,
  - correction magnitude,
  - rule dropout,
  - OOD generalization,
  - planning/control,
  - data-limited learning,
  - compute/runtime.
- Ensure all claims in the abstract have evidence in the paper.

Target sections:

- Evaluation
- Results
- Appendix

Priority: critical.

### 2.2 Report uncertainty and statistical significance

Source reviewers: R1, R2.

Problem:

- Error bars/standard errors are missing despite references to multiple seeds.
- Result interpretation may be invalid if differences are not statistically
  significant.

Required NeurIPS action:

- Report mean plus/minus standard error or confidence intervals for every main
  metric.
- State the number of seeds and what randomness varies across seeds.
- Add paired or unpaired statistical tests where appropriate, especially for
  close comparisons.
- Avoid claiming superiority when confidence intervals overlap strongly.

Target sections:

- Evaluation protocol
- Results tables
- Appendix / statistical tests
- Checklist

Priority: critical.

### 2.3 Explain post-prediction symbolic correction

Source reviewers: R1, R2.

Problem:

- The post-correction mechanism is described but apparently unused.
- It is unclear whether it applies only to NS-MAWM (Reg.) or also to other
  variants.
- If projection/residual already yield RVR=0, correction may be redundant.
- Calling it "lightweight" is unjustified.

Required NeurIPS action:

- Either remove the mechanism from the main method or explicitly include it as
  an ablation/baseline.
- Clarify when it is useful:
  - purely neural MAWM + post-correction,
  - NS-MAWM regularization,
  - diagnostic correction magnitude for projection.
- Explain that correction can be non-trivial and domain-dependent.
- Rename or qualify "lightweight" unless runtime evidence is provided.

Target sections:

- Method / post-correction
- Baselines table
- Results / correction magnitude
- Limitations

Priority: high.

### 2.4 Add robustness and generalization experiments

Source reviewers: R1, R3.

Problem:

- Rule ablation and unknown configurations are announced but not shown.
- The current validation is convincing only within structured environments.

Required NeurIPS action:

- Add rule-dropout experiments with several dropout rates.
- Evaluate unseen layouts, object configurations, agent counts, and/or SMAC
  scenarios.
- Report OOD MSE_H, OOD RVR, OOD return, and invalid plan rate.
- Interpret failures when rule coverage drops.

Target sections:

- Evaluation protocol
- Results
- Limitations

Priority: high.

### 2.5 Add data frugality / sample-efficiency evidence

Source reviewers: R1, R2.

Problem:

- The paper mentions frugality/data efficiency but does not show corresponding
  results.
- R1 asks for orders of magnitude for dataset sizes.
- R2 suggests "efficace en échantillons" is awkward phrasing.

Required NeurIPS action:

- Define dataset sizes N_small, N_med, N_full with actual numbers.
- Use nested replay subsets across methods.
- Report MSE_H, RVR, and return for each data regime.
- Present data-limited learning as an empirical claim, not a deductive
  guarantee.

Target sections:

- Evaluation protocol
- Results
- Appendix / hyperparameters

Priority: high.

### 2.6 Report compute and runtime

Source reviewers: R1, R3.

Problem:

- Execution duration is not discussed.
- Computational overhead and scalability are not quantified.

Required NeurIPS action:

- Report hardware, GPU type, CPU/memory if available, wall-clock time per run,
  and total experiment count.
- Compare inference/training overhead of neural baseline vs NS-MAWM variants.
- Discuss scaling with number of agents, feature dimension, and number of rules.

Target sections:

- Computing resources
- Results / efficiency
- Appendix / compute table
- Limitations

Priority: high.

## 3. Mathematical Formalization and Notation

### 3.1 Homogenize notation globally

Source reviewer: R2.

Problem:

- Variables are inconsistently indexed: agent index sometimes subscript,
  sometimes superscript.
- $a_x$ and $a_t$ conflict because x/t/i are not clearly assigned roles.
- $j$ is used without definition.
- Some indices start at 0 while formulas imply they start at 1.
- $\omega^d_t, \omega^u_t$ sometimes lose the agent index.
- $\hat{\omega}_{t+1}$ and projected/final outputs are conflated.

Required NeurIPS action:

- Add a notation table early.
- Define:
  - $i$ for individual agent index,
  - $j$ for joint quantities,
  - $t$ for time,
  - $k$ for feature index.
- Use one convention consistently: e.g., $\omega_t^i$ for agent observation,
  $\omega_t^j$ for joint observation.
- Use distinct names for raw neural prediction, symbolic prediction, projected
  prediction, residual prediction, and final prediction.
- Start feature indices at 1 unless there is a strong reason to use 0.

Target sections:

- Background
- Problem formulation
- Method
- Figure captions

Priority: critical.

### 3.2 Reorder definitions

Source reviewer: R2.

Problem:

- Hidden state $\mathcal{H}$ and recurrent state are used before being
  introduced.
- Sections 3.3 and 3.4 duplicate content and introduce concepts in a confusing
  order.
- It is unclear whether parts of Section 3 are background or contribution.

Required NeurIPS action:

- Put all background WM notation before the NS-MAWM method.
- Move contribution-specific definitions into the method/problem formulation.
- Add short transition paragraphs between section titles.
- Remove duplicated WM definitions.

Target sections:

- Background
- Problem formulation
- Method

Priority: high.

### 3.3 Simplify long formulas

Source reviewer: R2.

Problem:

- Long formulas with concat/flatten/unflatten are hard to read.
- Matricial notation is introduced but used only once.
- Some projection formulas may have dimension mismatches.
- Some equations equate raw neural output with final projected output.

Required NeurIPS action:

- Define compact operators for flatten/unflatten or remove them from the main
  text.
- Use a vector concatenation operator such as $\oplus$ if needed.
- Split decomposition equations into smaller equations:
  - full observation,
  - covered component,
  - residual component.
- Number key equations and reference them.
- Check all mask dimensions.
- Avoid using the same symbol for neural output and final output.

Target sections:

- Problem formulation
- Method / structured representation
- Method / projection and residual strategies

Priority: critical.

### 3.4 Define mathematical objects that reviewers flagged

Source reviewer: R2.

Objects requiring definition or clarification:

- $\Delta(A)$ as the simplex/distribution over actions.
- $\omega$ in the Dec-POMDP section.
- $\hat{P}_\phi$ and $\hat{R}_\phi$.
- $\mathcal{H}$ hidden/recurrent state space.
- $j$ as joint index/superscript.
- $f^k$ or $f_k$ feature notation.
- $\gamma^t$ and the finite/infinite horizon interpretation.
- one-hot prediction post-processing: argmax, threshold, or probability
  decoding.
- "cooldown-like constraints".
- "soft constraint" / "contrainte souple".
- "ambiguous" vs stochastic vs residual/non-deterministic.

Required NeurIPS action:

- Add these definitions explicitly in notation/problem/method.
- Avoid relying on MARL expertise from reviewers.

Priority: high.

## 4. Figures, Tables, and Visual Explanation

### 4.1 Fix method figure notation and semantics

Source reviewer: R2.

Problem:

- Figure 1 contains potential index errors.
- Some arrows appear inconsistent with the formulas.
- The meaning of green/orange and u/d components is unclear.
- The residual strategy may require a different neural architecture because its
  input is smaller.
- The figure is not always cited at the right place.

Required NeurIPS action:

- Replace the old figure with a simpler figure showing:
  - inputs,
  - semantic decomposition,
  - symbolic transition,
  - neural transition,
  - three coupling modes,
  - final prediction and metrics.
- Avoid using isolated "u" and "d" boxes without context.
- Explain clearly that residual dynamics uses a residual-output neural head or a
  different input/output interface.
- Cite the figure where the method is introduced.

Target sections:

- Method
- Figure caption

Priority: high.

### 4.2 Improve result table readability

Source reviewers: R1, R2.

Problem:

- Result table lacks standard errors.
- Abbreviations are inconsistent.
- The main takeaway is not visually emphasized.
- "RVR nul" is poor terminology.

Required NeurIPS action:

- Report mean plus/minus standard error.
- Use consistent method names.
- Bold best values only when statistically justified.
- Use "RVR=0" or "zero RVR" rather than "null RVR".
- Explain what the reader should conclude from each table.

Target sections:

- Results tables
- Captions

Priority: high.

## 5. Reproducibility and Code

### 5.1 Fix Overcooked/Gym dependency issue

Source reviewer: R2.

Problem:

- Overcooked demo failed because Gym is unmaintained and incompatible with
  NumPy 2.0.
- Reviewer suggests exact dependency versions in requirements.

Required NeurIPS action:

- Pin exact versions in the anonymous code archive.
- Prefer Gymnasium if migration is feasible.
- Add an environment file or lockfile.
- Add a smoke test command for every environment.
- State tested Python, NumPy, Gym/Gymnasium, PettingZoo, Overcooked-AI versions.

Target sections:

- Appendix / reproducibility
- Code archive
- Checklist

Priority: critical.

### 5.2 Strengthen reproducibility reporting

Source reviewers: R1, R2.

Problem:

- Code release is praised, but needs exact commands, versions, datasets, and
  environment details.

Required NeurIPS action:

- Provide one command per experiment family.
- Include configs for every environment/method/seed.
- Include exact data generation and preprocessing steps.
- Include rule files and mask computation.
- Include a final table mapping paper tables to commands.

Target sections:

- Appendix
- Code archive
- Checklist

Priority: high.

## 6. References and Bibliography

### 6.1 Rebuild bibliography

Source reviewer: R2.

Problem:

- Missing authors.
- First names and last names mixed.
- Missing venues.
- Missing conferences/journals.
- Bad capitalization for acronyms and model names.
- Weak or irrelevant metadata such as "OpenReview.net".
- Need to verify arXiv papers and published venues.

Required NeurIPS action:

- Audit every BibTeX entry.
- Prefer official proceedings BibTeX from publisher/DBLP/OpenReview when
  correct.
- Protect capitalization with braces: {MARL}, {MOISE+}, {SMAC}, {MBRL},
  {Dreamer}, etc.
- Remove unused references.
- Add missing venues and years.
- Check author completeness.

Target sections:

- references.bib

Priority: critical.

### 6.2 Add or strengthen missing citations

Source reviewers: R1, R2.

Candidate additions:

- PINNs / physics-informed neural networks for constraint integration analogy.
- Ontology-based rule extraction or domain knowledge.
- Variational inference for stochastic WMs.
- Gymnasium migration or dependency documentation if discussed.
- Cooldown/action-availability constraints if kept.

Priority: medium-high.

## 7. Writing, Terminology, and Style

### 7.1 Reduce anglicisms and define unavoidable English terms

Source reviewer: R1.

Problem:

- Many anglicisms: rollout, backbone, benchmark, layout.
- Some may be acceptable in English NeurIPS, but terms should be defined.

Required NeurIPS action:

- Since the NeurIPS version is in English, keep standard ML terminology but
  define it once.
- Avoid unexplained jargon.
- In French-derived notes, prefer:
  - "replay" as "replay buffer" in English,
  - avoid literal "rejouement",
  - avoid awkward "sample efficiency" translations.

Target sections:

- Full text

Priority: medium.

### 7.2 Fix punctuation and list formatting

Source reviewers: R1, R2.

Problem:

- Repeated ". ;", double semicolons, semicolon-separated lists containing full
  sentences.
- Excess punctuation in inline enumerations.

Required NeurIPS action:

- Use proper LaTeX lists when items are long.
- Use commas or semicolons consistently.
- Avoid sentence-ending periods inside inline enumerations.

Target sections:

- Introduction
- Method
- Evaluation

Priority: medium-high.

### 7.3 Homogenize terminology

Source reviewers: R1, R2.

Terms to homogenize:

- multi-agent / multi-agent systems / MARL.
- world model / World Model / WM.
- MAWM / NS-MAWM.
- symbolic/neural vs symbolic/numerical.
- covered/residual features rather than determinable/undeterminable.
- regularization, projection, residual dynamics.
- RVR_post = 0 rather than null RVR.

Priority: high.

### 7.4 Avoid excessive forward/backward references

Source reviewer: R2.

Problem:

- Many references to subsections make reading heavy.
- Mixed forward and backward references increase cognitive load.

Required NeurIPS action:

- Keep only necessary references to equations, tables, and figures.
- Avoid "as described in subsection X" immediately after the reader has seen the
  concept.
- Prefer local explanations.

Target sections:

- Method
- Implementation
- Evaluation

Priority: medium.

## 8. Detailed Local Corrections from JFSMA Reviews

These items are mostly local writing issues, but many indicate recurring
problems that should be avoided in the NeurIPS version.

### 8.1 Introduction

- Fix missing words in "rollouts degrade planning" type sentence.
- Avoid saying a "problematic prolongs previous work"; say the work builds on
  or extends previous work.
- If saying "several works", cite several works.
- Clarify G notation: in NeurIPS use G for gaps, not goals/verrous.
- Explain invariants/equivariances for readers not expert in MARL.
- Homogenize bolding of environment names such as SMAC.

### 8.2 Related work

- Avoid "more recent" when comparing works from the same year.
- Avoid bolding full paper titles in prose.
- Explain or remove claims such as "agents integrated into the environment
  implies stationarity".
- Clarify "In summary" transitions.

### 8.3 Background

- Add a short section-introduction sentence before subsections.
- Use itemized definitions for Dec-POMDP components.
- Define $\Delta(A)$ and $\omega$.
- Clarify finite/infinite horizon and discounting.
- Define model-based approximations $\hat{P}_\phi$, $\hat{R}_\phi$.
- Clarify assumptions behind sample complexity/sample efficiency statements.
- Add reference for variational inference if mentioned.

### 8.4 WM and MAWM notation

- Avoid conflicts between agent/time indices.
- Define hidden recurrent state before use.
- Clarify RNN/LSTM hidden state for non-specialists.
- Replace awkward terms such as "mapping" if needed.
- Add architecture schema or refer to the method figure.
- Define $T_\theta^j$ and $j$.
- Remove redundant formulas between single-agent WM and MAWM sections.
- Clarify whether section is background or method.

### 8.5 Structured observation and neuro-symbolic formalism

- Fix feature index ranges.
- Avoid ambiguous comma-heavy notation such as $f_{1,t},f_{2,t}$ if readability
  suffers.
- Keep agent indices consistently.
- Replace heavy matrix notation if not used later.
- Define a compact concatenation operator if useful.
- Avoid repeating the previous paragraph at the start of the next subsection.

### 8.6 Integration strategies

- Check $T_\theta$ vs $T_\theta^j$ consistency.
- Check $h_t^j$ vs $\tilde{h}_t^j$ consistency.
- Clarify whether residual dynamics uses a distinct neural architecture.
- Introduce $\hat{\omega}^{reg}$ and other variant-specific symbols before use.
- Ensure projection formula dimensions match.
- Avoid equating raw neural prediction with final projected prediction.
- Clarify "soft constraint".
- Do not confuse symbolic regularization with reward shaping unless making an
  explicit comparison.

### 8.7 Post-correction and RVR

- Explain purpose and scope of post-correction.
- Clarify whether post-correction applies to neural baseline, regularization,
  projection, residual, or all modes.
- Avoid claiming correction is lightweight unless measured.
- Define final decoding for one-hot outputs.
- Add raw neural prediction equation before RVR if needed.

### 8.8 Implementation

- Avoid relisting the three strategies repeatedly.
- Define $f_k$ in prediction loss.
- Clarify one-hot continuous output and final categorical decoding.
- Pin dependencies and address Gym/Gymnasium issue.
- Avoid excessive subsection references.

### 8.9 Evaluation

- Give actual dataset-size orders of magnitude.
- Clarify number of seeds/runs and what varies.
- Report standard errors.
- Add statistical tests.
- Avoid nested parentheses.
- Define rollouts.
- Use consistent abbreviations in tables.
- Bold best values only with caution.
- Explain close numerical differences and significance.

### 8.10 Conclusion and limitations

- Discuss:
  - manual rules,
  - domain ontologies,
  - LLMs only as one possible rule-generation route,
  - computational overhead,
  - scalability,
  - structured-environment bias,
  - opacity of residual neural dynamics,
  - trivial RVR_post for hard symbolic variants.

## 9. Action Checklist for NeurIPS Article

### A. Already partly addressed in the current NeurIPS draft

- NS-MAWM framed as the single contribution.
- Gaps reframed as theoretical gaps, not experimental apparatus.
- Deductive vs inductive claims separated.
- RVR_pre/RVR_post/correction magnitude introduced.
- Baseline and ablation table added.
- Claim-evidence registry added.
- Result-family scaffolds added for missing experiments.
- Limitations and broader impacts sections added.
- Checklist filled.
- Author block anonymized.
- Old method figure replaced by a simpler covered/residual diagram.
- One malformed BibTeX entry fixed.

### B. Still to implement in article.tex

1. Add/strengthen PINN/constrained-learning analogy in related work.
2. Add ontology/domain-rule extraction as future work.
3. Add exact data-size definitions for N_small, N_med, N_full.
4. Add exact compute/runtime table after final runs.
5. Clarify one-hot decoding and thresholds/argmax.
6. Clarify post-correction scope and possibly move it to ablations if not a
   core method.
7. Add statistical testing language and final test results.
8. Replace all symbolic placeholders in result scaffolds with final numbers.
9. Replace kappa placeholders with computed coverage ratios.
10. Add exact versions/licenses in the appendix.
11. Clean global notation and number key equations.
12. Reduce excessive subsection references.
13. Audit and rebuild the bibliography.

### C. Still to implement in code/supplement

1. Fix or pin Gym/Gymnasium/NumPy dependencies for Overcooked.
2. Provide exact environment files or lockfiles.
3. Provide smoke tests for all environments.
4. Provide scripts/configs for every table.
5. Export rule inventories and mask coverage computation.
6. Archive final seeds, configs, logs, and result aggregation scripts.

## 10. Suggested Modification Order

1. Formalization pass:
   notation table, equation numbering, index cleanup, projection/residual
   dimensional consistency.
2. Evaluation pass:
   claim-evidence registry, missing result tables, uncertainty/statistics,
   compute/runtime.
3. Reproducibility pass:
   dependency versions, commands, rule inventory, code archive synchronization.
4. Related-work pass:
   references, PINN analogy, ontologies, constrained learning.
5. Writing pass:
   terminology, punctuation, cross-reference reduction, table captions.
6. Final NeurIPS pass:
   anonymity, checklist consistency, page budget, layout.
