# NeurIPS Readiness Audit

This audit tracks whether the current draft follows the form and substance
expected from a competitive NeurIPS main-track submission. It is intentionally
strict: passing this audit means the paper is closer to a submit-ready artifact,
not merely a readable draft.

## 1. Official Format and Submission Constraints

Status: partially satisfied, with form/style improved in the latest pass.

- Uses the NeurIPS 2026 style file and anonymous author block.
- Includes references, appendix, and checklist in the expected order.
- Section titles, appendix titles, and method headings now follow a more
  conventional NeurIPS-style organization.
- Internal "pending" synchronization tables have been removed from the article
  and kept in the roadmap/audit documents instead.
- Current PDF is 36 pages after the latest pass; page-budget
  compression is intentionally deferred.
- The main text now uses bracketed numerical placeholders for all non-frozen
  quantitative fields. These are easy to locate and replace with final
  script-produced values.

Submission blocker:

- No bracketed numerical placeholder should remain in the submit-ready PDF
  unless it is deliberately kept as a notation convention rather than a value.

## 2. NeurIPS-Style Scientific Story

Status: strong draft.

- The paper now has a clear problem: semantic reliability of multi-agent world
  model rollouts under partial observability and partial symbolic coverage.
- The objective is decomposed into sub-objectives, then into three theoretical
  gaps.
- NS-MAWM is framed as the single contribution.
- Claims are separated by epistemic status: formal construction, conditional
  deductive guarantees, and empirical claims.

Remaining risk:

- The current abstract still announces the full empirical campaign. Before
  submission, every announced axis must have final numerical evidence.

## 3. Method Clarity

Status: good draft.

- Core notation table exists.
- Symbolically covered/residual decomposition is defined.
- Three integration modes are separated.
- RVR_pre/RVR_post/correction magnitude prevent misleading zero-RVR claims.
- Formal propositions state the exact conditional guarantee and error
  decomposition.
- Algorithmic pseudocode has been added to make the method reproducible.
- Vocabulary has been normalized toward "world models", "covered/residual
  features", "symbolic projection", "residual symbolic dynamics", and
  "semantic reliability".

Remaining risk:

- The bibliography and related-work comparison still need a final citation
  audit.

## 4. Experimental Standards

Status: structurally stronger after the NeurIPS-quality pass, numerically incomplete.

NeurIPS reviewers will expect:

- real results for every claim in the abstract/introduction;
- matched baselines under identical budgets;
- enough ablations to isolate symbolic regularization, projection, residual
  factorization, post-correction, and coverage;
- uncertainty across seeds;
- appropriate statistical tests or careful language when differences are close;
- exact rule coverage ratios and environment details;
- downstream planning/control if the paper claims MBRL utility.

Current draft:

- Has the validation matrix grouped by claim family, claim-evidence registry
  with overinterpretation warnings, claim-to-artifact traceability map,
  baseline table with reviewer objections, qualitative rollout audit,
  robustness/sensitivity paragraph, result schemas, and a submission
  synchronization gate.
- Does not yet have final synchronized numbers, exact kappa values, final plots,
  or final statistical tests.

Submission blocker:

- Replace draft aggregate values and working/final-run-required cells with
  script-produced final values before submission.

## 5. Reproducibility and Checklist Alignment

Status: stronger but not final.

- Appendix contains hyperparameter templates, rule inventory requirements,
  concrete local package versions/commits, compute templates, reproduction
  commands, submission synchronization gate, result provenance,
  related-work coverage audit, and code-audit status.
- Dependency issue around Overcooked/Gym/Gymnasium/NumPy is explicitly flagged.
- Checklist is present and mostly aligned with the intended final state.
- Local code audit: 7/8 tests pass; the failing test is a synthetic
  training-loss fixture shape issue, while rule-engine, projection, and RVR
  checks pass.

Remaining risk:

- Checklist answers must be re-audited after the final code archive is frozen.
  In particular, reproducibility, open access, statistics, compute, and licenses
  should not say "Yes" unless exact values/commands/assets are actually present.

## 6. Ethics, Limitations, and Societal Impact

Status: good draft.

- Broader impacts discusses auditability and misplaced trust.
- Limitations discuss rule coverage, misspecified masks, manual or domain-specific
  symbolic representations, residual opacity, scalability, hidden variables,
  low-coverage regimes, and overconfidence.

Remaining risk:

- Add final quantitative evidence about compute overhead and rule authoring
  burden if available.

## 7. Highest-Priority Remaining Tasks

1. Finish the downstream planning/control experiment first. This is the most
   important remaining NeurIPS blocker because it turns semantic reliability
   into decision relevance.
2. Regenerate horizon-sweep logs for H=1, 10, 25, and 50, then replace the
   bracketed error-accumulation table with script-produced curves.
3. Regenerate RVR_pre/RVR_post/correction-magnitude distributions, including
   median and 95th percentile correction magnitudes.
4. Add at least one strong WM baseline (RSSM/Dreamer-style) and one structured
   rule-feature baseline in the actual experiment configs, not only in the text.
5. Replace all bracketed numerical placeholders with final experimental outputs.
6. Compute and insert exact kappa coverage values and rule counts from the
   implemented masks.
7. Insert final OOD, rule-dropout, noisy-rule, and data-limited results.
8. Run paired statistical tests and report effect sizes where needed.
9. Freeze dependency versions and smoke-test all environments.
10. Audit every BibTeX entry and remove unused references.
11. Re-audit checklist answers against the final archive.
12. Compress main content to the NeurIPS page budget.

## 7b. NeurIPS Reviewer Response Roadmap

The latest strict NeurIPS-style review moves the draft from "promising but not
fully convincing" toward a paper that must demonstrate meaningful impact, not
only cleaner consistency metrics. The corresponding action plan is:

- Core impact: make the paper's main empirical claim "semantic reliability
  improves world-model behavior" rather than "semantic metrics improve." The
  downstream MPC/CEM planning table is now the central test of this claim.
- Empirical depth: report horizon-wise MSE/RVR curves, invalid-transition
  rates, failure-case visualizations, and correction-magnitude distributions.
- Baselines: instantiate the RSSM/Dreamer-style WM baseline and the structured
  rule-feature WM baseline under matched budgets.
- Method clarity: keep one-sentence intuitions and trade-offs for
  regularization, projection, and residual symbolic dynamics in the method.
- Rule specificity: report rule counts, representative rules, mask-derived
  coverage ratios, and scalability cost O(n |R| c).
- Robustness: include at least one OOD or partial-observability shift and at
  least one rule-dropout/noisy-rule stress test.
- Statistical rigor: use at least five seeds, mean +/- standard error, matched
  seed comparisons, and effect sizes for close conclusions.
- Figures: convert the error-accumulation and qualitative-rollout audit tables
  into one clear rollout-comparison figure and one horizon-vs-error plot before
  the final page-compression pass.

## 8. Current Non-Synchronized Result Artifacts

The following paper artifacts are intentionally still placeholder-level and must
be replaced with script-produced outputs before submission:

- Bracketed aggregate values in `tab:results_overview` and per-environment
  MSE values in `tab:per_env_prediction`.
- Bracketed horizon-sweep, semantic-drift, invalid-transition, rule-dropout,
  planning/OOD, and data-limited values.
- Bracketed coverage ratios and rule counts.
- Exact wall-clock times and total compute.
- Any textual claim in the abstract or introduction that depends on final
  numerical outcomes.

Estimated readiness for scientific submission: about 91% before final
experiments/code-freeze/page-compression; structural readiness is about 98%.
