# Rebuttal notes

One entry per reviewer criticism: a 1–3 sentence response usable as-is,
plus the pointer to the fix. Grouped as **Corrected** (the criticism was
right, fixed as described), **Weakened as requested** (fixed by making a
narrower claim rather than a technical correction), and **Judgment call**
(addressed, but by combining/choosing among the options offered rather
than picking exactly one — noted so you can override if you'd have chosen
differently). There is no **Disagree** category: on review, every
criticism in the report was correct as stated: the corollary genuinely
conflated two readings of one bound, the independence assumption really
was missing, the T5 construction really was ambiguous under the paper's
own formalism, and so on. We looked for a defensible counter-argument on
each point before fixing it and did not find one worth making.

---

## Part A — Mathematics

**A1 (Theorem 5.1 independence).** *Corrected.* The `ln(1/δ)/N_c` bound
assumed i.i.d. violation indicators without stating so, and treated `N_c`
as fixed without justification. Assumption 5.1 now states both regimes
explicitly (episode-subsampled i.i.d., or an any-time-valid test-
supermartingale argument valid under correlation and adaptive stopping),
with a full proof in `supplementary.tex` citing Howard et al. (2020).
→ `paper.tex` §5 (Assumption 5.1, Theorem 5.1); `supplementary.tex` §Full proofs.

**A2 (Theorem 5.2, which policy does the certificate concern).**
*Corrected.* F2–F4 certify against gate-specific policies `π_2,π_3,π_4`,
not the passive `π`; the theorem now states a per-gate certificate with
an explicit union bound over (candidate, gate) pairs, and states plainly
that this bound is what licenses reusing `D_test` adaptively across
gates — a property the original statement left the reader to infer.
→ `paper.tex` §5 (Theorem 5.2), Algorithm 1.

**A2, re-promotion.** *Judgment call.* The task offered "require fresh
data" or "cap at `R_max`" as alternatives; we adopted both (fresh data as
the primary control, `R_max` as a bounded safety net against unbounded
cycling), since they address different failure modes and are not
mutually exclusive. If you want only one, dropping the `R_max` cap is the
smaller of the two to remove.

**A3 (threshold/grid search into the budget).** *Corrected.* No longer
deferred: `M̂_eff` folds in the `τ_soft/τ_hard/m_max/β` grid explicitly,
with the observation that this is cheap (log-cost) rather than a reason
to avoid it. → `paper.tex` §5 (Eq. for `M̂_eff`), conclusion.

**A4 (Corollary 5.3, linear vs. logarithmic).** *Corrected.* The
corollary's "linear, not logarithmic" framing conflated a fixed-budget
false-discovery *count* (genuinely linear in `M̂_eff`) with a fixed-error
*sample-size* requirement (logarithmic, same as Theorem 5.2, not in
tension with it). Rewritten with `prec_prop` and the corrected
certification-budget comparison (`1.56×`, not `10^4×`). This was the
single most consequential fix in Part A — the abstract's headline framing
of why a parsimonious proposer helps was built on it. → `paper.tex` §5
(Corollary 5.3), every downstream invocation (abstract, intro, §7.2,
§7.5); `supplementary.tex`.

**A5.4 (does the corridor example instantiate Theorem 5.6?).** *Corrected,
provisionally — needs your sign-off.* As literally constructed, the
example was ambiguous-leaning-incoherent under the paper's own
joint-observation formalism. We replaced the confound with a genuinely
latent, no-observation-channel environment hazard, which is unambiguous.
See `revision/QUESTIONS.md` for the alternative fix (restrict `φ` to
per-agent-local readings) if the confound was meant to be specifically
about inter-agent privacy rather than latency in general.
→ `supplementary.tex` (corridor construction + note), vocabulary fix
throughout `paper.tex`.

**A5 (missing related work, missing positive result).** *Corrected.*
Added the offline-RL concentrability (Chen & Jiang 2019) and OPE-under-
confounding (Namkoong et al. 2020) positioning — both verified via
independent search before citing — and a new Theorem 5.7 (sufficient
condition for transfer: certification against the gate-policy mixture
plus finite concentrability of the deployment policy transfers with
bounded degradation). §5 is now the 5.5→5.6→5.7 triptych requested.
→ `paper.tex` §2, §5; `supplementary.tex` (Theorem 5.7 proof, upgrading
the previously-unlabeled "Positive counterpart" proposition).

**A6 (Theorem 5.4, vacuity, Figure 2 misattribution).** *Corrected.*
Downgraded to Proposition 5.4 (hidden Assumption of rollout support,
unestablished), and the bound is now explicitly flagged as vacuous beyond
a horizon this draft cannot compute since `L` is never estimated
(`\todoval`, TODO-EXPERIMENTS item 9). Figure 2's caption no longer
attributes the observed saturation to the proposition. → `paper.tex` §5,
Figure 2 caption; `supplementary.tex`.

**A7 (Theorem 5.5 numeric example, F4 claim).** *Corrected.* The example
conflated `C_{π'/π}(c)` with `Pr_π[c]/Pr_{π'}[c]`; replaced with two
independent, explicit numbers. The claim that F4 "estimates `C_{π'/π}(c)`"
is replaced with the correct, and frankly stronger, claim that F4
estimates `ε^{π'}` directly. → `paper.tex` §5 (discussion after Theorem 5.5).

**A8 (Remark composition, missing `Pr[c_i]`; `κ` vs. `κ_eff`).*
*Corrected.* The union bound now correctly includes `Pr[c_i]`; the
dramatic "50 rules → `ε_d≤0.5`" claim was an artifact of the missing
factor (corrected: `≈0.05` at typical precondition frequency). Turned
into a measured, per-rule `τ_hard` calibration rule. Added the `κ`/`κ_eff`
distinction, flagged as not currently measured (`\todoval`, TODO-
EXPERIMENTS item 7) rather than papered over. → `paper.tex` §5–6;
`supplementary.tex`.

## Part B — Experimental

**E1 (undefined metric).** *Corrected* (a specification gap, since no code
exists to look the definition up in). Defined as a per-seed-paired AUC
ratio with an explicit degenerate-denominator policy, shipped with a
recomputation script. → `revision/QUESTIONS.md`, `revision/scripts/`.

**E2 (5 seeds don't support the claimed comparisons).** *Weakened as
requested.* Computed real `t`-statistics; only P1 vs. P2/P3 clears
`|t|≥1.96`. Every other claim ("P2 edges out P3," "closes a third of the
gap") is rewritten to "no detectable difference at 5 seeds." Flagged the
paired-seed bootstrap as the highest-yield follow-up. → `paper.tex` §7.2
(new), §7.4, §7.5.

**E3 (transfer results in prose, no table).** *Corrected.* Moved to
`tab:transfer` with SE and significance; the abstract's headline numbers
are now explicitly scoped to GridCraft. → `paper.tex` §7.2 (new).

**E4 (ladder claim on one table line).** *Weakened as requested.* The
conclusion no longer asserts the ladder is "load-bearing" from a single
row; states what the row shows and specifies (in-paper + TODO-EXPERIMENTS)
the three experiments that would support the general claim.
→ `paper.tex` §7.3, conclusion.

**E5 (no baseline comparison).** *Weakened as requested, and specified.*
Added the "What this section does not establish" paragraph explaining why
system-to-system comparison (WALL-E, SAM) isn't directly meaningful but a
fixed-proposer, varied-certification-mechanism ablation is, and specified
that ablation in full. → `paper.tex` §7.5; `revision/TODO-EXPERIMENTS.md` item 5.

**E6 (missing reproducibility numbers).** *Corrected (specification);
values remain TODO-EXPERIMENTS.* New §7.6 lists every missing quantity
with `\todoval`, plus the contamination discussion with two concrete
mitigations. → `paper.tex` §7.6.

**E7 (`RVR_pre` under Residual; matching criterion; coverage asymmetry).**
*Corrected.* All three now defined explicitly, including why `RVR_pre`
being identical between the conditioned/unconditioned residual rows is
expected (both are computed on covered features, where the two variants
don't differ), not an error. → `paper.tex` §6, §7.1, §7.4.

**E8 (typos).** *Corrected.* Section 7.3's title bug and the French
`ε_cible` residual were caught and fixed during A6/A8; a subsequent sweep
of both files found nothing else.
