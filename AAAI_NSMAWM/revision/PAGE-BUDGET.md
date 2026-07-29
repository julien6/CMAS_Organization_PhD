# Page budget

**Current state:** `paper.tex` compiles to **12 pages** (content through
page 11, References starting mid-page-11 and finishing on page 12).
AAAI's limit is **9 pages total** (7 content + 2 references). We are
**≈3.5–4 pages over content budget**. Per the task's rule 1 ("propose the
cuts in `revision/PAGE-BUDGET.md` without applying them — author's
decision"), nothing below has been applied to `paper.tex`.

This overflow is expected and is the direct, line-item cost of correcting
the mathematical and experimental issues in the reviewer report: every
chantier in Part A added an Assumption, a corrected statement, or a new
theorem; every chantier in Part B added a table, a significance
computation, or a specification paragraph the paper previously lacked.
None of it is padding. The question this document answers is which of it
can move to `supplementary.tex` (already unlimited in length and already
carries the full proofs) without weakening the main paper's argument, not
which of it should be deleted.

## Where the added length is (approximate, by chantier)

| Addition | Approx.\ length | Currently | Could move to supplement? |
|---|---|---|---|
| Assumption 5.1/5.2 (A1, A6) | ~6 lines | `paper.tex` §5 | Partially — keep 1-sentence statement, move regime (b)'s derivation detail (already largely in supplementary) |
| Per-gate certificate + budget definition (A2/A3) | ~12 lines | `paper.tex` §5 | No — this is the corrected core claim, belongs in the main paper |
| Corollary 5.3 rewrite (A4) | ~8 lines net (was already present, restructured) | `paper.tex` §5 | No — same reason |
| Theorem 5.7 + triptych discussion (A5) | ~10 lines | `paper.tex` §5 | Partially — the triptych *statement* should stay, the extended discussion sentence could shorten |
| Related-work paragraph (A5) | ~6 lines | `paper.tex` §2 | Yes, safely — could compress to 3 lines citing both works in one sentence |
| Proposition 5.4 discussion + vacuity remark (A6) | ~5 lines | `paper.tex` §5 | No — this is exactly the correction the reviewer required be visible |
| `tab:significance` + discussion (E2) | ~20 lines (table + prose) | `paper.tex` §7 (new subsection) | **Yes** — table could move to supplementary with only the headline conclusion ("only P1 vs. P2/P3 is significant") kept in the main text |
| `tab:transfer` + discussion (E3) | ~18 lines (table + prose) | `paper.tex` §7 (new subsection) | **Yes** — same treatment as above |
| Ladder-experiment specification paragraph (E4) | ~7 lines | `paper.tex` §7.3 | Yes — could compress to 2 lines + pointer to TODO-EXPERIMENTS.md |
| "What this section does not establish" (E5) | ~6 lines | `paper.tex` §7.5 | Yes — could compress to 2 lines + pointer |
| §7.6 Experimental details (E6) | ~10 lines (mostly `\todoval` list) | `paper.tex` §7.6 (new) | **Yes, largely** — the `\todoval` list is exactly appendix material; keep only the contamination paragraph (a substantive point) in the main text |
| `RVR_pre`/matching/asymmetry definitions (E7) | ~10 lines | `paper.tex` §6–7 | Partially — the Residual `RVR_pre` clarification should stay (it explains an otherwise-confusing identical-numbers artifact in Table 4), the matching-threshold and asymmetry notes could shorten |

## Recommended cut sequence (highest-value-per-line-saved first)

1. **Move `tab:significance` and `tab:transfer` to the supplement**,
   keeping one sentence each in the main text ("see supplementary Table
   S1/S2 for the full significance analysis and transfer-environment
   breakdown; only P1's disadvantage against P2/P3 clears `|t|≥1.96`").
   Estimated savings: **~0.6–0.8 page**.
2. **Move §7.6 (Experimental details) to the supplement almost entirely**,
   keeping only the contamination paragraph (a substantive limitation,
   not a bookkeeping item) in the main text with a one-line pointer for
   the rest. Estimated savings: **~0.3 page**.
3. **Compress the E4/E5 specification paragraphs** to 2 lines each with a
   pointer to `TODO-EXPERIMENTS.md` instead of describing the three/one
   experiments inline. Estimated savings: **~0.25 page**.
4. **Compress the A5 related-work paragraph** to 3 lines. Estimated
   savings: **~0.1 page**.
5. **Trim the Theorem 5.7 discussion paragraph** to state the triptych in
   one sentence rather than three. Estimated savings: **~0.1 page**.

Applying 1–5 would save an estimated **1.3–1.5 pages**, which is not
enough by itself to reach 7 content pages from the current ~10.5; the
remainder would have to come from trimming the pre-existing method
sections (§3–4) that this revision did not touch, which is a genuinely
different kind of decision (cutting explanatory content vs. moving
verification/appendix material) and is left entirely to you.

## What we did not consider cutting

The corrected theorem statements, the new Theorem 5.7, the honest
significance table's *conclusion* (even if the table itself moves), and
the weakened ladder/baseline claims are the actual content of this
revision. Cutting any of them to hit a page count would reintroduce
exactly the problems the reviewer report identified. If the 7-page limit
must be hit without further seed-generating experiments, the realistic
path is: apply cuts 1–5 above, then shorten §3 (Background) and §4.2
(transport catalog), which were not touched by this revision and are the
most compressible remaining material, since their content is largely
also available in `supplementary.tex`'s §Transport catalog and
precondition language.
