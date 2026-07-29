# Theorem map

Built before any revision edit, from `paper.tex` (as of the pre-revision commit) and
`supplementary.tex`. Numbering follows the shared `theorem` counter, reset per section
(`\newtheorem{theorem}{Theorem}[section]`); `corollary`, `remark`, etc. share that counter,
so the printed numbers in Section 5 are: Thm 5.1, Thm 5.2, Cor 5.3, Thm 5.4, Thm 5.5,
Thm 5.6, Remark 5.7 — even though the internal LaTeX labels are `thm:t1, thm:t2, cor:t2b,
thm:t3, thm:t4, thm:t5` (non-matching label/number order; a maintenance hazard flagged here
so it isn't rediscovered mid-revision).

| Printed # | Internal label | Name |
|---|---|---|
| Thm 5.1 | `thm:t1` | Certification by survival |
| Thm 5.2 | `thm:t2` | Search cost |
| Cor 5.3 | `cor:t2b` | Expected false discoveries |
| Thm 5.4 | `thm:t3` | Chaining to rollout fidelity |
| Thm 5.5 | `thm:t4` | Degradation under policy shift |
| Thm 5.6 | `thm:t5` | Non-identifiability under partial observability |
| Remark 5.7 | (unlabeled) | Composition |

Supplementary mirrors: `thm:t1-full, thm:t2-full, cor:t2b-full, thm:t3-full, thm:t4-full,
thm:t5-full` in `supplementary.tex`, plus an unlabeled `Proposition [Positive counterpart]`
after the Thm 5.6 proof and an unlabeled `Remark [Composition, full derivation]`.

---

## Thm 5.1 — Certification by survival (`thm:t1`)

- **Stated**: `paper.tex:230-233`.
- **Proved**: `supplementary.tex:127-134` (`thm:t1-full`), via `(1-\varepsilon_r)^n \le e^{-\varepsilon_r n}`.
  Uses i.i.d. Bernoulli assumption on violation indicators conditional on `N_c=n` — **no
  assumption block states this in the main text**; it is asserted in supplementary prose
  ("Notation" paragraph, `supplementary.tex:125`) rather than as a numbered assumption.
  `N_c(r)` itself is treated as fixed/conditioned-on without justifying that conditioning
  doesn't bias the argument beyond one sentence. **This is A1.**
- **Invoked**:
  - `paper.tex:91` (intro, informal restatement).
  - `paper.tex:178` ("This separation is what makes Thm 5.1 and 5.2 apply to `D_test`
    without selection bias") — correct use, about the partition discipline.
  - `paper.tex:188` (Algorithm 1, step: "compute `\hat\varepsilon_r` and confidence `q_r`
    (Thm 5.1, 5.2)") — correct, both used for the confidence formula.
  - `paper.tex:231` — is the statement itself (self-reference via numbering).
  - `supplementary.tex:59` (data-partition discussion, correctly scoped).
  - `supplementary.tex:141` (proof of Thm 5.2, applies Thm 5.1 at level `\delta/\hat M`
    per candidate — correct use provided A1's fix is inherited, see A1 action).

## Thm 5.2 — Search cost (`thm:t2`)

- **Stated**: `paper.tex:236-239`.
- **Proved**: `supplementary.tex:136-142` (`thm:t2-full`), union bound over `Thm 5.1` at
  level `\delta/\hat M`.
- **Invoked**:
  - `paper.tex:91` (intro).
  - `paper.tex:156` (transport catalog: "restrict `\rho` ... to keep the search space small
    enough for Thm 5.2 to bind usefully").
  - `paper.tex:178` (partition discipline, with Thm 5.1).
  - `paper.tex:188` (Algorithm 1 step).
  - `paper.tex:237` (statement).
  - `paper.tex:331` (§7.2 discussion — **misuse to check**: text says P1's low precision
    is evidence "consistent with Thm 5.2... rather than the weaker, merely logarithmic
    union-bound cost of Thm 5.2" — internally consistent since it correctly attributes the
    *log* cost to Thm 5.2 and contrasts it with Cor 5.3's linear-in-`\hat M` false-discovery
    argument. Not a misuse, but depends on Cor 5.3 being correctly stated — see A4).
  - `paper.tex:429` (conclusion, "the transport catalog trades expressivity against Thm
    5.2's union-bound cost" — correct, high level).
  - `supplementary.tex:59, 99, 137` (definition and proof context).
- **A2/A3 dependency**: Thm 5.2 as stated is about `D_test`-only certification (F1). It says
  nothing about what happens once F2 (adaptive, `D_test`-reusing) is applied, nor does it
  fold in threshold/grid search over `\tau_soft, \tau_hard, m_max, \beta`. Both A2 and A3
  modify this theorem's hypotheses and conclusion; every invocation above must be re-checked
  once `\hat M` becomes `\hat M_eff` (A3) and once the guarantee is stratified by gate (A2).

## Cor 5.3 — Expected false discoveries (`cor:t2b`)

- **Stated**: `paper.tex:241-244`. Contains the sentence **"linear, not logarithmic, in
  `\hat M`"** and the follow-up sentence at `paper.tex:245` with the `10^6` vs `10^2`
  numeric illustration.
- **Proved**: `supplementary.tex:146-154` (`cor:t2b-full`). Also contains the same "linear,
  not logarithmic" framing at `supplementary.tex:144` ("A weaker argument... shrinks this
  bound by reducing `\hat M`... This is not, by itself, a strong argument. The stronger
  argument is on the expected count...").
- **Invoked** (this is where the false claim propagates — **A4 must fix all of these**):
  - `paper.tex:91` (intro): "the expected number of false discoveries growing *linearly* in
    that number — which is the argument for using a parsimonious proposer".
  - `paper.tex:331` (§7.2): "as expected if a much larger `\hat M`... inflates the number of
    low-quality survivors at a fixed falsification budget, rather than the weaker, merely
    logarithmic union-bound cost of Thm 5.2" — **this sentence conflates "false-discovery
    count at fixed budget" (correctly linear in `\hat M`) with "P1 has lower precision than
    P2/P3" as if the corollary alone explained precision. It does not: precision also
    depends on proposal precision, which the corollary does not model (A4a).**
  - `paper.tex:422` (§7.5 ablations): "is well below what Cor 5.3 would project for P1's
    much larger `\hat M` at the same budget, consistent with P2/P3's smaller candidate pool
    doing the work the corollary attributes to it" — same conflation.
  - `paper.tex:429` (conclusion): no direct mention, but the whole "search-cost argument" of
    the abstract (`paper.tex:75`) rests on this corollary.
  - `supplementary.tex:154`: repeats the `10^6`/`10^2` numeric illustration.
- **A4 must**: rewrite the corollary statement and proof to separate the *fixed-budget*
  count bound (linear in `\hat M`, correct) from the *fixed-error* sample-budget comparison
  (logarithmic in `\hat M`, i.e., **not** in opposition to Thm 5.2 but the same dependency
  read differently), add the proposal-precision decomposition, and then fix every
  invocation listed above (they currently read as if a parsimonious proposer's advantage is
  explained by the corollary alone).

## Thm 5.4 — Chaining to rollout fidelity (`thm:t3`)

- **Stated**: `paper.tex:247-250`. States one-step bound and, "under an L-Lipschitz rollout
  operator," the H-step bound `E_H \le (\sum_{i=0}^{H-1} L^i)(\varepsilon_d B^2 + e_u)`,
  explicitly flagged as conditional on an assumption "not a guarantee."
- **Proved**: `supplementary.tex:156-163` (`thm:t3-full`); Assumption (H) explicitly marked
  false in general right below the proof.
- **Invoked**:
  - `paper.tex:91` (intro, "a chaining bound from discovery validity to long-horizon
    rollout fidelity").
  - `paper.tex:373` (**Figure 2 caption — the problematic one**): "M tracks B2 more closely
    than B1 throughout and reaches roughly 0.21 vs. B1's 0.52 at H=100, consistent with
    Thm 5.4" and, in the body text discussion just above at `paper.tex:355`
    ("`\autoref{fig:compounding}` follows the downstream consequence... into the rollout
    itself"). **A6 problem**: with `L>1` the RHS is exponential in H and is not "consistent
    with" anything observed at H=100 — the bound is vacuous there. The observed
    saturation is a property of the bounded observation space (errors cannot exceed the
    feature-space diameter), not a consequence of the theorem.
  - `paper.tex:429` (conclusion): "Thm 5.4's chaining argument assumes imagined rollouts
    stay within the falsification distribution's support, which we could not establish as
    a theorem" — this is honest about Assumption (H) but does not address the `L`/vacuity
    problem, which is separate.
- **A6 must**: downgrade to Proposition (conditional), name Assumption (H) explicitly as a
  numbered assumption, add the vacuity remark (bound only informative for `L<1` or
  `H \lesssim \ln(1/(\varepsilon_d B^2+e_u))/\ln L`), and rewrite the Figure 2 caption to
  stop attributing the observed saturation to the theorem.

## Thm 5.5 — Degradation under policy shift (`thm:t4`)

- **Stated**: `paper.tex:252-255`.
- **Proved**: `supplementary.tex:165-172` (`thm:t4-full`).
- **Invoked**:
  - `paper.tex:91` (intro).
  - `paper.tex:151` (§4.1, "a fact we treat formally in Thm 5.5 and Thm 5.6").
  - `paper.tex:253` (statement).
  - `paper.tex:256` (**the flawed numeric illustration — A7**): "a rule certified at
    `\varepsilon^\pi_r=0.01` transfers... at `\varepsilon^{\pi'}_r \le 0.02` whenever `\pi'`
    visits the precondition region at least half as often as `\pi`... relative to the
    worst-case density ratio" and "gate F4... is a direct empirical estimate of
    `C_{\pi'/\pi}(c)`". Both clauses are imprecise per the reviewer (A7).
  - `paper.tex:429` (conclusion): "Thm 5.5 bounds, but does not eliminate, degradation
    under policy shift" — fine, high level.
  - `supplementary.tex:108` (falsification gate F4 description, cites `thm:t4-full`).
  - `supplementary.tex:213` (Positive counterpart proposition, "in the sense of
    `thm:t4-full`" — correct use, this is exactly the concentrability object A5's Thm 5.7
    should build on).

## Thm 5.6 — Non-identifiability under partial observability (`thm:t5`)

- **Stated**: `paper.tex:258-261`, with the constructive proof pointer to supplementary.
- **Proved**: `supplementary.tex:174-198` (four-cell corridor construction + impossibility
  argument), corollary "Memory is not a remedy" at `supplementary.tex:196-198`, comparison
  table (deferred effect vs. latent confounder) at `supplementary.tex:200-210`, and the
  unlabeled "Positive counterpart" proposition at `supplementary.tex:212-214`.
- **Invoked** (highest invocation density of any result in the paper — consistent with the
  reviewer calling it "the paper's central negative result"):
  - `paper.tex:75` (abstract), `91` (intro summary), `95` (intro, evaluation protocol
    paragraph), `97` (intro, section roadmap: "conclusion discusses... consequences of
    Thm 5.6"), `108` (related work, WALL-E paragraph: "Our non-identifiability result
    applies to their setting as much as to ours"), `151` (§4.1), `221` (caption of Fig. 1
    pipeline diagram — the red "T5" box), `259` (statement), `262` (discussion paragraph
    right after the theorem — deferred-effect/confounder framing, motivates F1-F4 ladder),
    `307` (§7.1 setup, difficulty gradient description), `355` (§7.3 discussion of Table 3
    last row — **this is where the reviewer's A5.4 coherence question bites hardest**: text
    says "a rule over another agent's never-observed private state" and "the confounding
    agent does occupy the previously-unvisited region"), `427, 429` (conclusion, twice).
  - `supplementary.tex:111` (Algorithm step, memory-order test), `175` (statement), `224`
    (extended protocol, difficulty gradient description — same "another agent's private
    observation" phrasing as the main text).
- **A5 must resolve first**: whether "agent 2's position," as constructed, is genuinely
  outside the joint observation `\omega^j` the discovery procedure reads `\varphi` from
  (Definition, `paper.tex:139-144`: "a reading `\varphi` of **the joint observation**"). If
  agent 2 observes its own position (the natural Dec-POMDP reading, since nothing in the
  construction says otherwise), then `x^2 \in \omega^2 \subset \omega^j`, and a
  joint-observation reading `\varphi` *could* include it — contradicting the theorem's
  claim that no certification procedure with access to `d^\pi` can recover it. **This is
  case (ii) in the assignment's terms: literally as written, the example does not
  obviously instantiate the theorem it illustrates.** See `revision/QUESTIONS.md` for the
  full resolution write-up (this file only maps *where* the problem surfaces, not the
  resolution — per the task's own procedure, A5.4 is resolved before further edits).
- Every location above that uses the phrase "another agent's private observation" /
  "another agent's never-observed private state" is a candidate for the vocabulary fix
  ("a latent environment variable never entering any agent's observation") **once and only
  once A5.4 is resolved** — do not edit piecemeal before that.

## Remark 5.7 — Composition (unlabeled in `paper.tex`, `Remark [Composition, full
derivation]` in supplementary)

- **Stated**: `paper.tex:264-266`.
- **Full derivation**: `supplementary.tex:216-218`.
- **Invoked**:
  - `paper.tex:265` itself contains the flawed bound `\varepsilon_d \le \sum \varepsilon_{r_i}`
    (missing `\Pr[c_i]` factor — **A8**) and the dramatic "50 rules at 0.01 already gives
    `\varepsilon_d \le 0.5`" claim, plus "reframes the coverage-saturation pattern reported
    for `\kappa \to 1`... as a consequence of uncontrolled aggregate error."
  - `supplementary.tex:217`: same missing factor, plus the malformed/French-residue
    expression `1-\varepsilon_{\mathrm{cible}}/p` (also present at `paper.tex:265`).
- **A8 must**: fix the union-bound derivation (`\varepsilon_d \le \sum_i \varepsilon_{r_i}
  \Pr[c_i]`), recompute the numeric illustration, fix the calibration formula for
  `\tau_hard`, and add the `\kappa` vs. `\kappa_{eff}` distinction (not currently invoked
  anywhere — this is a **new** definitional gap, not a misinvocation, so it needs a new
  paragraph in §4/§6 plus a new column candidate in Table 3, not just a fix at this
  Remark's location).

---

## Cross-cutting invocation risk not tied to a single theorem

- **§7 (`sec:exp`) numeric narrative** repeatedly writes "consistent with Cor 5.3" /
  "consistent with Thm 5.2" / "as predicted by Thm 5.4" as connective tissue between
  theory and numbers that were, in the current draft, authored illustratively rather than
  measured (see prior revision turns). Once A1-A8 change what several theorems actually
  claim, **every one of these connective phrases in §7 must be re-read against the new
  statement**, not just patched locally — this is why the task's final step ("relis le
  papier entier") is treated as its own item below rather than folded into the per-theorem
  fixes.
- The **Figure 1 pipeline diagram** (`paper.tex:197-223`) has a box literally labeled
  "survives F1 only ⇒ suspect confound (T5)" — this is a second, purely visual invocation
  of Thm 5.6 that must track whatever vocabulary fix A5.4 requires (e.g., if the fix is
  "latent environment variable," the box text should not say "agent 2" but it currently
  does not say that explicitly, so likely no change needed here — verified during A5 pass).
