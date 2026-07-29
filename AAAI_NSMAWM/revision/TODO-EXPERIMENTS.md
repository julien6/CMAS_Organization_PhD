# Missing experiments, ranked by decreasing yield

"Yield" = how much of the paper's current argument changes once this
experiment lands, not how hard it is to run. Each entry: what to run, on
what, how many seeds, which table/figure it fills, which claim it
unblocks. None of these can be run from this repository (no experiment
code exists anywhere in the workspace — see `revision/code_map.md`); this
file is the specification to hand to whoever implements the discovery
algorithm and environments.

---

## 1. Paired-seed bootstrap re-analysis of Table 2 / Table 4

**What:** if the 5 seeds used for each proposer (P1/P2/P3) and each
injection strategy are *matched* (same environment instantiation/initial
conditions, only the discovery/injection component varied), recompute
every comparison in `tab:significance` as a paired-seed bootstrap
(resample seed indices with replacement, compute the paired difference
each time) instead of the current unpaired `t`. Paired analysis cancels
common-seed noise and can turn several of the currently-non-significant
comparisons (P2 vs. P3, residual-conditioning fix, projection vs.
residual) into detectable effects, or confirm they really are noise.
**Cost:** zero new environment interaction — pure re-analysis of logs that
would already exist. **Seeds:** reuses the existing 5; a follow-up at
≥15 seeds (see item 6) would need paired logs regardless.
**Fills:** `tab:significance`, and every claim built on it in §7.2–§7.5.
**Unblocks:** whether "P2 edges out P3" and "the residual-conditioning fix
helps" can be stated as findings rather than "no detectable difference."

## 2. F1-only vs. F1–F4 ablation on `fraction recovered` directly

**What:** run the full discovery pipeline (P2 default) twice per
environment: once certifying only through F1 (passive holdout), once
through the full F1–F4 ladder, and compare `fraction recovered` between
the two — not the binary certified/non-certified outcome currently
reported in `tab:gradient`. This is the experiment the paper's central
protocol claim ("the falsification ladder is load-bearing, not just the
proposer") is not currently tested against.
**Cost:** 2× the existing discovery runs per environment (F1-only is a
subset of the F1–F4 run, so this is closer to +0% compute, +bookkeeping).
**Seeds:** 5, same protocol as Table 2.
**Fills:** a new table alongside `tab:gradient`, referenced from §7.3.
**Unblocks:** the conclusion's ladder claim, currently deliberately
weakened pending this result.

## 3. Systematic confound-detectability sweep tied to Theorem 5.7

**What:** plant `N` latent confounds of varying detectability, parameterized
by how often the confounding region is visited under the passive
policy `π` (e.g., visit frequency `∈ {0, 0.01, 0.05, 0.1, 0.3}`), and plot
detection rate (correctly flagged as non-certifiable) against the
falsification-policy family's empirical coverage of that region —
directly testing Theorem 5.7's sufficient condition (`C_{π'/\barπ}(c)<∞`)
rather than illustrating it with the one hand-planted example in
`tab:gradient`.
**Cost:** moderate — requires instrumenting GridCraft (or another
environment) to plant confounds with controllable visit frequency; the
falsification protocol itself is unchanged.
**Seeds:** 5 per confound-detectability level.
**Fills:** a new figure (detection rate vs. coverage), referenced from
§7.3 and Theorem 5.7's discussion.
**Unblocks:** turning Theorem 5.7 from a proven-but-unillustrated positive
result into an empirically validated one; this is the single experiment
that would make the paper's "triptych" (5.5→5.6→5.7) fully load-bearing
rather than partially load-bearing on the theory side alone.

## 4. Interaction-budget accounting for F2 (active exploration)

**What:** report the number of additional environment steps F2's
active/directed exploration costs relative to F1's passive holdout, in
the same units as the wall-clock comparison already in `tab:ablations`,
per environment. A severity ladder that is only affordable in
GridCraft's cheap-to-reset regime is a materially weaker claim than one
that holds at comparable interaction budgets in Overcooked/SMACv2, where
resets are not free.
**Cost:** low — this is a logging addition to the existing F2
implementation, not a new experiment.
**Seeds:** 5, reusing existing runs.
**Fills:** a column in `tab:ablations` or a new small table.
**Unblocks:** whether the ladder's benefit survives being priced in the
same currency as its cost.

## 5. P2 + WALL-E-style heuristic pruning vs. P2 + F1–F4 (fixed proposer)

**What:** hold the proposer fixed (P2) and replace `alg:main`'s
falsification gates with a WALL-E-style induce/prune heuristic (keep a
rule if not contradicted by a bounded window of recent trajectories,
prune by maximum coverage, no statistical validity bound). Run on the
same environments and the same `fraction recovered` metric as Table 2.
**Cost:** moderate — requires implementing the heuristic baseline, which
is simpler than the falsification protocol it replaces.
**Seeds:** 5, matched to Table 2's protocol.
**Fills:** a new row/table in §7.5, referenced from the new "What this
section does not establish" paragraph.
**Unblocks:** the single most dangerous gap for acceptance per the
reviewer report — without it, the paper asserts but does not demonstrate
that falsification with an explicit bound beats heuristic induce/prune.

## 6. Re-run Table 2 / Table 4 at ≥15 seeds

**What:** the same protocol, more seeds. Power calculation from the
currently-observed SDs: for the P2-vs-P3 gap (`0.837` vs. `0.774`,
implied per-seed SD `≈0.039×√5≈0.087` and `≈0.057×√5≈0.127`, pooled
`SD≈0.109`), detecting a true difference of `0.063` at `α=0.05` two-sided
with power `0.8` requires `n≈2·(1.96+0.84)²·SD²/Δ² ≈ 2·7.84·0.01193/0.00397
≈ 47` seeds per arm — substantially more than the 15 a first pass might
budget for, which only detects effects `≳0.11` at the same power. Report
this honestly rather than treating 15 seeds as sufficient by assumption.
**Cost:** high (compute-bound, scales with seed count).
**Fills:** every table in §7.
**Unblocks:** upgrading "suggestive" to "established" for the borderline
comparisons (P2 vs. P3 on SMACv2 specifically, `t=1.94` at 5 seeds, is the
closest to significance and the cheapest to firm up first).

## 7. `κ_eff` (transition-level coverage) alongside `κ̂`

**What:** compute, per proposer/environment, the fraction of covered
positions whose precondition is actually true at each transition
(Remark, "Feature coverage vs. transition coverage"), not just the
feature-space coverage ratio `κ̂` currently reported.
**Cost:** low — a logging addition, computable from data already produced
by the falsification pipeline (precondition truth values are already
evaluated per transition).
**Seeds:** 5, reusing existing runs.
**Fills:** a new column in Table 2.
**Unblocks:** correctly interpreting Theorem 5.4/Proposition 5.4's
disjoint-covered/residual assumption, which is stated in feature space but
used in transition space.

## 8. Experimental-details numbers (§7.6)

**What:** log and report, for the existing protocol (no new runs needed):
`N_c(r)` distribution per gate, `p` (number of simultaneously hard-injected
rules), exact sizes of `D_prop/D_fit/D_test/D_shift`, the realized
`τ_soft/τ_hard/m_max/β` grids feeding `M̂_eff`, P3's exact model
identifier/version/temperature/cost/prompt, and the retrogradation-rate
denominator (total steps, rules at risk).
**Cost:** zero new compute — pure logging/reporting discipline once the
pipeline exists.
**Fills:** §7.6's `\todoval` markers (7 of the current 10).
**Unblocks:** a reviewer being able to recompute Theorem 5.1/5.2/Corollary
5.3's bounds from the paper's own numbers, which is currently impossible.

## 9. Lipschitz constant `L` of the rollout operator

**What:** estimate `L` (empirically, e.g., via finite-difference
sensitivity of the rollout operator to input perturbations) per
architecture and environment, to determine whether Figure 2's `H=100` is
inside or outside Proposition 5.4's informative range.
**Cost:** low-moderate — a standard Lipschitz-estimation procedure, not a
new training run.
**Fills:** the `\todoval` in Proposition 5.4's discussion.
**Unblocks:** knowing whether Figure 2's observed saturation pattern is
even in principle explainable by Proposition 5.4, as opposed to being
entirely a property of the bounded observation space (our current best
guess, stated as such).

## 10. Precision/recall sensitivity to the rule-matching threshold

**What:** recompute Table 2's precision/recall at the `95%` semantic-
match threshold and at exact syntactic match, alongside the `99%`
threshold currently used, to show how much of the reported precision/
recall is an artifact of the matching criterion.
**Cost:** zero new runs — recomputation from existing discovered-rule and
oracle-rule logs.
**Fills:** a sensitivity table in §7.1/§7.2.
**Unblocks:** ruling out (or in) that the matching-threshold choice is
doing unstated work in the headline precision/recall numbers.
