# Revision changelog

One item per chantier. Format: problem → what changed → where → status.
Git history has one commit per chantier (`git log --oneline` in this
directory); this file is the human-readable index into that history.

## Reconnaissance

- **theorem_map.md / code_map.md**: built before any edit. Confirmed no
  experiment code exists anywhere in the workspace (only a hand-transcribed
  GridCraft table from an unrelated JFSMA presentation). Status: **done**.

## E1 / A5.4 (handled first, per the task's own procedure)

- **E1 — `fraction recovered`'s underlying quantity was never specified.**
  Defined as a per-seed-paired AUC ratio of the compounding-error curve
  (Figure 2's quantity) over `H∈[0,100]`, with a degenerate-denominator
  exclusion rule and across-seed SE on the ratio itself. Shipped as a
  runnable script with a synthetic self-test.
  Where: `revision/QUESTIONS.md` (§E1), `revision/scripts/compute_fraction_recovered.py`, `paper.tex` §7.1.
  Status: **done** (not blocking — a specification gap, not a lookup failure).
- **A5.4 — does the four-cell corridor example instantiate Theorem 5.6?**
  Found the literal construction ambiguous-leaning-incoherent (case (ii)):
  "agent 2's position" is plausibly part of the joint observation the
  discovery procedure reads from. Documented in `revision/QUESTIONS.md`,
  applied the recommended fix (replace the confound with a genuinely
  latent, no-observation-channel environment hazard) provisionally, and
  flagged for author sign-off — the alternative fix (restrict `φ` to
  per-agent-local readings) is also described there if you intended the
  confound to be inter-agent-privacy-specific.
  Where: `supplementary.tex` (corridor construction), `revision/QUESTIONS.md`.
  Status: **applied, pending your sign-off** (see Questions below).

## Part A — Mathematics

- **A1 (Theorem 5.1).** Missing independence assumption and unjustified
  treatment of `N_c` as non-random. Added Assumption 5.1/5.2 (own counter,
  doesn't renumber Theorem/Corollary) with two regimes: episode-subsampled
  i.i.d. (exact original bound) and an any-time-valid test-supermartingale
  regime (Howard, Ramdas, McAuliffe, Sekhon 2020; verified before citing),
  valid under within-episode correlation and adaptive stopping at the cost
  of a small `O(log log N_c)` inflation. Full martingale proof in
  `supplementary.tex`.
  Status: **done**.
- **A2 (Theorem 5.2).** F2–F4 collect data under different policies
  (`π_2,π_3,π_4`), not the original `π`; the original statement wrote a
  single `ε^π_r` regardless of gate. Restated as a per-gate certificate
  (`ε^{π_k}_r`) with an explicit union bound over `M̂_eff × K` (candidate,
  gate) pairs, and made explicit that this is what licenses reusing
  `D_test` adaptively across F1→F4 — a strength of the protocol that was
  previously invisible. Re-promotion after retrogradation now requires
  fresh data and is capped at `R_max`, both folded into the budget and
  documented in Algorithm 1.
  Status: **done**.
- **A3 (search-cost budget).** The conclusion's "we defer resolving this
  formally" about threshold/grid search leaking into `M̂` is fixed instead
  of deferred: `M̂_eff = M̂ × |grid(τ_soft)| × |grid(τ_hard)| × (m_max+1) ×
  |grid(β)|`, folded into Theorem 5.2 and Corollary 5.3, with the
  observation that this is cheap (logarithmic cost) rather than a reason
  to avoid it.
  Status: **done**.
- **A4 (Corollary 5.3).** Conflated "expected false-discovery count is
  linear in `M̂`" with "certification cost is logarithmic in `M̂`" as if
  in tension. Rewritten to separate the two readings explicitly, introduce
  `prec_prop` (proposer precision) so the bound is
  `(1-prec_prop)·M̂_eff·e^{-ε*N}` rather than `M̂_eff·e^{-ε*N}`, and add the
  correct certification-budget comparison (`N_c≈1378` for P1 vs. `≈882`
  for P2, factor `1.56`, not `10^4`). Fixed every downstream invocation
  (abstract, intro, §7.2, §7.5, supplementary's "weaker argument"
  paragraph and worked example).
  Status: **done**.
- **A5 (Theorem 5.6 + related work + Theorem 5.7).** See A5.4 above for
  the construction fix. Added the missing related-work positioning
  (offline-RL concentrability, Chen & Jiang 2019; OPE under unobserved
  confounders, Namkoong et al. 2020) and a new Theorem 5.7 (sufficient
  condition for transfer: certification against the falsification-gate
  mixture plus finite concentrability of the deployment policy against
  that mixture bounds transfer). §5 now reads as the requested triptych:
  5.5 (degradation, conditional) → 5.6 (impossibility, coverage can fail)
  → 5.7 (sufficiency, coverage restores the guarantee).
  Status: **done**, modulo A5.4's sign-off.
- **A6 (Theorem 5.4 → Proposition 5.4).** Downgraded (own hidden
  Assumption of rollout support, unestablished) and fixed the vacuity gap
  (`L>1` makes the H-step bound exponential and uninformative beyond a
  horizon this draft cannot compute, since `L` is never estimated —
  flagged with `\todoval`). Figure 2's caption no longer claims the
  observed saturation is "consistent with" or "predicted by" the
  proposition; attributed to the bounded observation space instead.
  Status: **done**.
- **A7 (Theorem 5.5 numeric example + F4 claim).** The worked example
  conflated `C_{π'/π}(c)` with `Pr_π[c]/Pr_{π'}[c]`, forcing an
  inconsistent regime. Replaced with two independent, explicit numbers
  (`C=4`, ratio `=0.5`) giving the same headline `0.02`. Fixed the false
  claim that F4 "is a direct empirical estimate of `C_{π'/π}(c)`" — F4
  estimates `ε^{π'}` directly (stronger), not the unobservable supremum
  density ratio.
  Status: **done**.
- **A8 (Remark 5.8, Composition).** Union bound omitted `Pr[c_i]`
  (`ε_r` is conditional on `c_i`, so `Pr[V_i]=ε_i·Pr[c_i]`, not `ε_i`
  alone), making "50 rules → `ε_d≤0.5`" an artifact of the missing
  factor. Fixed in both files, turned into a per-rule `τ_hard`
  calibration rule driven by each rule's own measured trigger frequency.
  Added the `κ` vs. `κ_eff` (feature-space vs. transition-space coverage)
  distinction Theorem 5.4/Proposition 5.4's "disjoint masks" assumption
  actually needs, flagged via `\todoval` rather than invented (not
  currently computed in any table).
  Status: **done**; `κ_eff` numbers are a TODO-EXPERIMENTS item.

## Part B — Experimental (writing + specification)

- **E1.** See above.
- **E2 (significance).** Computed real (unpaired) `t` for every
  proposer/strategy comparison directly from the means/SEs already in
  Table 2/4. Only P1 vs. P2/P3 clears `|t|≥1.96`; rewrote every other
  claim ("P2 edges out P3", "closes roughly a third of the gap") to "no
  detectable difference at 5 seeds." Flagged a paired-seed bootstrap as
  the single highest-value follow-up (in TODO-EXPERIMENTS.md).
  Status: **done** (statistics correct given the current numbers;
  superseded once real per-seed logs exist).
- **E3 (transfer results).** Moved out of prose into `tab:transfer` with
  SE and the same significance treatment; scoped the abstract's headline
  numbers to GridCraft explicitly.
  Status: **done**.
- **E4/E5 (ladder claim, no baseline).** Weakened "the falsification
  ladder is load-bearing" to what one planted-confound row actually
  supports; specified (in-paper pointer + full protocol in
  TODO-EXPERIMENTS.md) the three missing ladder experiments and the
  missing P2+WALL-E-style-pruning vs. P2+F1–F4 ablation.
  Status: **specification done, experiments not run** (no code exists to run them).
- **E6 (missing reproducibility numbers).** New "Experimental details"
  subsection (§7.6) lists every quantity needed to audit §5's bounds from
  this paper's own numbers that isn't reported, each flagged with
  `\todoval` (10 total, see page-1 counter): `N_c(r)` distribution, `p`,
  partition sizes, threshold/grid cardinalities, P3's model/prompt/cost,
  retrogradation denominator, `κ_eff`, precision/recall at other matching
  thresholds. Added a contamination paragraph (anonymization strips
  names, not structure) with two concrete mitigations.
  Status: **done** (specification); values are TODO-EXPERIMENTS items.
- **E7 (definitional gaps).** Defined `RVR_pre` under Residual dynamics
  (a diagnostic-only auxiliary head, not the deployed model — explains
  why it's identical between conditioned/unconditioned rows by
  construction); defined the semantic-equivalence threshold for matching
  discovered rules to oracle rules; added the false-positive-vs-false-
  negative coverage cost asymmetry under hard injection.
  Status: **done**.
- **E8 (typos).** Section 7.3's title bug ("exercises Theorem 5.5" for
  Theorem 5.6 content) and the French `ε_cible` residual were both fixed
  incidentally during A6/A8. Swept the rest of both files; nothing else found.
  Status: **done**.

## Infrastructure

- Added a `\todoval{}` marker (via the `totcount` package, after a
  hand-rolled aux-counter approach broke on a `@`-catcode subtlety when
  writing to the `.aux` file) with a running total displayed on page 1,
  distinct from Section 7's authored illustrative results.
- Fixed a latent build gap: `supplementary.tex` had no citation package or
  bibliography wired up before this revision (nothing had cited anything
  there). Added `natbib` + `plainnat` + `references.bib`.
- Fixed a counter-sharing bug introduced mid-revision: the first version
  of Assumption 5.0 shared the `theorem` counter, silently renumbering
  every subsequent Theorem/Corollary by one. Caught before committing by
  re-checking rendered numbering against the reviewer's own references;
  gave assumptions their own counter instead.

## Not attempted / explicitly out of scope

- No renaming of Theorem 5.6 to "Corollary of Theorem 5.5" (the task
  offered this as optional "if you keep the numbering"; kept as Theorem
  5.7 alongside 5.5/5.6 instead, to avoid a full renumbering cascade
  through every cross-reference and every external document — QUESTIONS,
  theorem_map, this changelog — that cites the reviewer's original
  numbers).
- Page budget: not trimmed. See `revision/PAGE-BUDGET.md`.
