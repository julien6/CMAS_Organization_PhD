# Open questions requiring the author's decision

Two items were flagged by the task as potentially blocking (E1, A5.4) and had to be
resolved before touching §5/§7. Both are resolved below; only one (A5.4) is a genuine
author decision point and is presented as such — the fix is applied provisionally so the
rest of the revision isn't stalled, but it changes the *narrative example* instantiating
Theorem 5.6, not the theorem itself, and deserves your sign-off before it goes further
(e.g., before you generate any real GridCraft rule matching it).

---

## A5.4 — Does the four-cell corridor example actually instantiate Theorem 5.6? [DECISION NEEDED]

### The problem, stated precisely

Theorem 5.6 claims non-identifiability of a rule's validity from data generated under a
single policy `π`, when the underlying Dec-POMDP has a component that is genuinely
unavailable to the certification procedure. The certification procedure, per the paper's
own **Definition (Partial invariant)** (`paper.tex:139-144`), operates on a reading `φ` of
**the joint observation `ω^j`**, and the reading catalog (`paper.tex:153-156`,
`supplementary.tex:61-67`) explicitly ranges over `f_{i,k}` for **every agent `i` and every
feature `k`** — i.e., `φ` has access to every agent's own observation, not just agent 1's.

The four-cell corridor construction (`supplementary.tex:178-198`) says: *"Agent 1's
observation is only its own position `x^1`; it never observes agent 2's position."* It says
nothing about what agent 2 itself observes. Two readings:

- **(i) Genuinely latent.** Agent 2 also never observes its own position `x^2` — i.e.,
  `x^2` is a component of the global state `s` but of *no* agent's observation space, so
  `x^2 \notin \Omega^1 \cup \Omega^2`, hence `x^2 \notin \omega^j` for any joint observation.
  Under this reading, `φ` (which only reads `ω^j`) truly cannot see `x^2` under any
  circumstance, and the theorem's construction is coherent with the paper's own formalism.
- **(ii) Merely private to agent 1.** Agent 2 observes its own position `x^2` (the default,
  unremarked-upon assumption in the rest of this same paper: `paper.tex:147-149`
  describes agent features as "relative position, object type, health..." with no
  suggestion that an agent cannot observe its own state), so `x^2 \in \omega^2 \subset
  \omega^j`. Under this reading, a discovery procedure with access to the **joint**
  observation — which is exactly what the Definition grants it — could in principle include
  `x^2` in a candidate reading `φ`, and the "confound" is then a limitation of *which*
  readings the proposer happened to search (a scoping choice, e.g. "GridCraft's
  already-factorized features" restricting proposers to per-agent-local features), not a
  fact about observability. This would make the current wording ("another agent's
  never-observed private state," `paper.tex:355`, `paper.tex:427`) **false as stated under
  the paper's own Definition** — precisely the incoherence the task instructions describe
  as case (ii).

### Finding

As **literally constructed**, the corridor example is reading (ii): nothing in
`supplementary.tex:178-198` places `x^2` outside every agent's observation space, and the
paper's own convention elsewhere (features include an agent's own position) makes reading
(ii) the *natural* default, not reading (i). This is a real inconsistency between the
theorem's claim (non-identifiability from `d^\pi`, where `d^\pi` is a distribution over
**joint** transitions) and its worked example (an argument that only holds if a *specific*
per-agent observation channel is blind to `x^2`, which is a weaker and different claim than
"no joint-observation-based procedure can see it").

### Recommended fix (applied provisionally below; needs your sign-off)

Change the construction from "agent 2's position" to a **genuinely latent state variable**
that enters neither agent's observation function by construction — e.g., a hidden
"blocking" flag `b_t \in \{0,1\}` that is part of the global state `s_t` (it determines
whether cell `k{+}1` is passable) but is **never emitted by any `O(\omega^i \mid s', a^j)`**,
for any `i`. This is a one-line change to the construction (state space augmented with `b_t`
instead of "agent 2 is present"; the "policy" `\pi` vs. `\pi'` becomes a distribution over
`b_t`'s trajectory rather than over agent 2's trajectory) and:

- Makes the theorem and example consistent under the paper's own `φ(\omega^j)` formalism
  (this is now unambiguously case (i)).
- Preserves every downstream claim (deferred-effect-vs-confounder table, "memory is not a
  remedy" corollary, the positive counterpart proposition) essentially verbatim, since
  none of them depend on the confound being *another agent* specifically.
- Requires a vocabulary pass everywhere "another agent's private observation" is used:
  `paper.tex:95, 260, 307, 355, 427`; `supplementary.tex:224`; and the Table 3 row label
  "Multi-agent private obs." (`paper.tex:349`) should become something like "Latent
  environment confound (planted)" — **the class stops being about multi-agent
  observability specifically**, which also removes the informal claim that this is a
  distinctively *multi-agent* failure mode (it is a partial-observability failure mode that
  is easy to construct in a multi-agent setting, but is not intrinsically about other
  agents).

**This is applied in the A5 commit below**, with the vocabulary and the corridor
construction both updated. If you intended the confound to specifically be about
inter-agent privacy (e.g., because the real GridCraft rule you have in mind for the
difficulty gradient genuinely is "requires observing another agent's position, which
GridCraft's observation function withholds by design"), then the fix is different: instead
of changing the example, add a sentence to the Definition restricting `φ` to
**per-agent-local** readings by default (with joint readings as an explicit, separately
falsified extension), which would make reading (ii) load-bearing instead of broken — i.e.,
the "confound" would then correctly be about restricted proposer scope, and the theorem
would need a companion statement about *that*. **Tell me which of the two you want**; I
went with the first (latent state variable) because it changes less of the paper and
requires no new theorem, but the second may better match what you actually want to claim
about GridCraft's real observation function once it exists in code.

---

## E1 — What does `fraction recovered` actually measure? [RESOLVED, not blocking]

No code exists in this repository to inspect (see `revision/code_map.md`), so this is a
specification decision, not a lookup. Resolved as:

> `fraction recovered = (Err_{AUC}(B_1) - Err_{AUC}(M)) / (Err_{AUC}(B_1) - Err_{AUC}(B_2))`,
> where `Err_{AUC}` is the area under the open-loop compounding-error curve (mean squared
> per-feature prediction error over the joint observation, Figure 2's y-axis) over rollout
> horizons `H \in \{0,\dots,100\}`, computed **per seed** with matched environment seeds
> across `B_1`, `B_2`, `M` (same seed ⇒ same environment instance/initial conditions for all
> three), then averaged across the 5 seeds with the reported standard error being the
> across-seed SE of the **per-seed ratio** (not a delta-method approximation of a ratio of
> means, and not a single ratio computed from already-averaged numerator/denominator).

Rationale for AUC over an endpoint: a single-horizon snapshot (e.g., `H=100` alone) is
noisier and throws away the rest of the curve; using AUC is also why the table's fraction
recovered (e.g., `0.837` for the residual strategy) does not have to numerically match a
naive endpoint-only computation from Figure 2's `H=100` values (which gives `\approx 0.79`
using `(0.52-0.21)/(0.52-0.13)`) — the two are related but not identical statistics, and
the difference is now explained rather than silently inconsistent.

**Degenerate-denominator policy**: a seed is excluded from the ratio computation (and the
exclusion count reported) if `Err_{AUC}(B_1) - Err_{AUC}(B_2) < 0.05 \times Err_{AUC}(B_1)`
(oracle rules provide negligible measurable benefit for that seed/environment instance);
the raw numerator (absolute error reduction) is always reported alongside the ratio so a
reader can sanity-check that exclusions are not hiding a systematically small denominator.

**Recomputation script**: `revision/scripts/compute_fraction_recovered.py` implements this
exactly (per-seed paired ratio, exclusion rule, across-seed SE) against a CSV schema
(`seed, environment, model, horizon, error`) and includes a synthetic self-test reproducing
the Table 2 / Figure 2 aggregates used in this draft, so that once real per-seed logs exist
they can be dropped in without changing the statistical procedure.

This definition is written into `paper.tex` §7.1 (see `fix(exp-metric)` commit).
