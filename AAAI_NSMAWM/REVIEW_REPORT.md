# Pre-submission adversarial review — AAAI-27

Reviewer persona: AC looking for a desk-reject motive + 3 hostile-but-competent
reviewers + reproducibility engineer + format/anonymity reviewer.
Files reviewed: `paper.tex`, `supplementary.tex`, `references.bib`,
`aaai2027.sty`/`.bst`, `ReproducibilityChecklist.tex`, `Figures/`,
compiled `paper.pdf`/`supplementary.pdf`/`ReproducibilityChecklist.pdf`.
Not available / not verifiable: experiment code (confirmed absent, see
`revision/code_map.md`), AAAI-27 submission-portal-level items (conflicts of
interest, LLM-disclosure checkbox) — flagged NON VÉRIFIABLE where relevant.

Venue/deadline (per author confirmation): AAAI-27, abstract submitted
2026-07-21, full paper due 2026-07-28 23:59 UTC-12, reviewed 2026-07-29.
Rules extracted from https://aaai.org/conference/aaai/aaai-27/submission-instructions/
and https://aaai.org/conference/aaai/aaai-27/main-technical-track-call/ (fetched
live, not from memory).

---

## PASSE 1 — Conformité formelle

| ID | Sév. | Emplacement | Constat | Preuve | Correctif | Effort |
|---|---|---|---|---|---|---|
| P1-01 | BLOCKER | Whole doc | 12 pages vs. 9-page hard limit (7 content + 2 refs) | `pdfinfo paper.pdf`: Pages 12; references start mid-page-11 | See `revision/PAGE-BUDGET.md` cut list + trim §3/§4.2 | half day |
| P1-02 | MINOR | L309-310 | Overfull hbox 19.7pt (κ_eff paragraph) | `paper.log`: "Overfull \hbox (19.73894pt too wide)" | Rephrase/shorten the sentence | 5 min |
| P1-06 | QUESTION | L221,231,461,463 | `\scriptsize` used inside TikZ/pgfplots figure annotations (not body/table text) | grep | Confirm legibility at print size; not a body-text violation | — |
| P1-07 | QUESTION | `supplementary.tex` L1-19 | Supplementary uses plain `article` class with `geometry`+`hyperref`, both forbidden in the *main* paper by `aaai2027.sty`'s guard, but supplementary is not bound by that class | Read of preamble | Confirm AAAI's supplementary format has no equivalent restriction (not found in fetched CFP text) | — |
| — | checked | — | Fonts: all Type 1, embedded, subset. No forbidden packages, no `\vspace{-}`, `\newpage`, `\clearpage`, `\baselinestretch`, `\setlength`. Page size 612×792 (US Letter). No PDF metadata leak. | `pdffonts`, greps, `pdfinfo` | — | — |

**1 BLOCKER / 0 MAJOR / 1 MINOR**

## PASSE 2 — Audit d'anonymat

| ID | Sév. | Emplacement | Constat | Preuve | Correctif | Effort |
|---|---|---|---|---|---|---|
| P2-01 | BLOCKER | L96,104,145,306,314,339,350 | Branded, un-cited self-system name "NS-MAWM", framed with "our own"/"our prior" possessives 6+ times | `grep -n "NS-MAWM" paper.tex` (6 hits, 0 citations) | Cite anonymously, or strip the proper noun and first-person framing entirely | 30-60 min |
| P2-02 | BLOCKER | L333-334, L339 | "prior review cycles of this project", "earlier review of this line of work", "earlier version of this work" — explicitly reveals a resubmission history to reviewers | Direct quotes | Rewrite as self-contained corrections with no review/version references | 20 min |
| P2-04 | MINOR | `supplementary.tex` L18 | `hyperref` loaded in supplementary; checked PDF metadata (exiftool) — Author/Title fields blank, no leak found in practice | `exiftool supplementary.pdf` | Low risk as-is; could still drop hyperref for consistency | 5 min |
| — | checked | — | `\author{Anonymous Submission}` correct in both docs; no acknowledgments section; no grant/institution text; only non-identifying URL found is a public JAX GitHub link in the bibliography | greps, exiftool | — | — |

**2 BLOCKER / 0 MAJOR / 1 MINOR** — this is, jointly with P1-01, the most severe pass in the review: AAAI treats anonymity failures as automatic desk-reject material.

## PASSE 3 — Audit des affirmations

| ID | Sév. | Emplacement | Constat | Preuve | Correctif | Effort |
|---|---|---|---|---|---|---|
| P3-01 | MAJOR | L306 (Remark, Composition) | "an order of magnitude **looser** than $\sum_i\varepsilon_{r_i}$ alone suggests" — but the corrected bound (0.05) is *smaller* than the naive sum (0.5), i.e. **tighter**, not looser. Word inversion contradicts the math it's describing. | Recomputed: $50\times0.01=0.5$ vs. corrected $0.5\times0.1=0.05$; $0.05<0.5$. | Replace "looser" with "tighter" | 2 min |
| P3-02 | MAJOR | Abstract L84, Intro L102 | Both say "we give **five** results", enumerating survival/search-cost/chaining/degradation/non-identifiability — Theorem 5.7 (sufficient condition for transfer), a real, proved, positive result added this revision and heavily discussed as closing the "triptych" (§5), is absent from both counts. | Text comparison, abstract vs. §5's seven labeled results (5.1,5.2,Cor5.3,Prop5.4,5.5,5.6,5.7) | Add a clause mentioning Thm 5.7 to the abstract's and intro's contribution list | 15 min |
| — | checked | — | Title/abstract/intro/conclusion internally consistent otherwise; no unsupported "first"/"significantly"/"robust"-without-evidence overclaims found beyond the transfer-environment "robustness" hint already covered under P5-01 | Full read | — | — |

**0 BLOCKER / 2 MAJOR**

## PASSE 4 — Rigueur technique et mathématique

| ID | Sév. | Emplacement | Constat | Preuve | Correctif | Effort |
|---|---|---|---|---|---|---|
| P4-01 | MAJOR | Assumption `ass:support`, Prop. 5.4 | Proposition 5.4 (chaining) rests on Assumption 5.2 ("rollout support"), which the paper itself states is unestablished ("we could not show ... we treat it as a conjecture"). Honestly disclosed, but leaves Prop. 5.4 without a demonstrated regime of validity. | L276-285 | Already correctly downgraded to a Proposition; recommend explicitly stating in the rebuttal that this is a known open gap, not glossing over it if asked | — |
| P4-02 | MINOR | Table 1 (`tab:catalog`) vs. §5 | $\delta_a$ (transport-family free parameter) and $\delta$ (certification failure probability in Thm 5.1/5.2/Cor 5.3) are visually close notation in nearby sections | Read-through | Consider renaming one (e.g., $\delta_a\to b_a$) | 20 min |
| — | checked | — | Theorem/proof correspondence with `supplementary.tex` matches `revision/theorem_map.md` (independently spot-checked, not re-derived line by line here); Howard et al. 2020 citation for the any-time-valid claim verified as a real paper via web search this session | — | — | — |

**0 BLOCKER / 1 MAJOR / 1 MINOR**

## PASSE 5 — Validation empirique

| ID | Sév. | Emplacement | Constat | Preuve | Correctif | Effort |
|---|---|---|---|---|---|---|
| P5-01 | BLOCKER | `tab:transfer`, L427 | SMACv2 row's $t=1.94$ is arithmetically wrong; correct value is $t=1.41$. Predator–Prey's $t=0.10$ should be $\approx0.13$. This directly undercuts the paper's own "borderline... just short of 1.96" narrative and the speculative "P3 more robust" hypothesis it supports. | Independent recomputation (Python, shown twice) | Fix table + prose; correct reading is "no detectable difference on any transfer environment" | 30 min |
| P5-02 | MAJOR | Entire §7 | No experiment code or logs exist anywhere in the workspace; every number is an authored illustrative value (already disclosed via `\todoval` counter and `revision/CHANGELOG.md`, but still the paper's largest empirical weakness) | `revision/code_map.md` | Run the experiments (`revision/TODO-EXPERIMENTS.md`, ranked) | new experiments |
| P5-03 | MAJOR | §7.5 "What this section does not establish" | No baseline vs. WALL-E/WALL-E-2.0 or SAM-family, self-disclosed | L522 | `TODO-EXPERIMENTS.md` item 5 | new experiment |
| P5-04 | MAJOR | All tables | $n=5$ seeds; paper's own power calculation shows ~47 needed for the P2-vs-P3-class comparisons | `TODO-EXPERIMENTS.md` item 6 | Re-run at higher $n$ | new experiments |
| P5-05 | MINOR | §7.1 | Precision/recall sensitivity to the 99% matching threshold not reported (self-flagged) | L352, `\todoval` | `TODO-EXPERIMENTS.md` item 10 | recompute only |

**1 BLOCKER / 3 MAJOR / 1 MINOR**

## PASSE 6 — Reproductibilité

| ID | Sév. | Emplacement | Constat | Preuve | Correctif | Effort |
|---|---|---|---|---|---|---|
| P6-01 | BLOCKER | `ReproducibilityChecklist.tex` | All 31 questions unanswered ("Type your response here" ×34, 0 real answers found) | scripted scan | Fill in honestly (mostly "no"/"NA" given no code) | 1-2h |
| P6-02 | BLOCKER | §7 | No code/data anywhere; "could a competent PhD student reproduce Table 2?" — No. | `revision/code_map.md` | Disclose in checklist; cannot be fixed before this deadline | — |
| P6-03 | MINOR | Whole doc | No code/data availability statement or license mentioned anywhere, anonymized or otherwise | grep, full read | Add one sentence even if "not yet released" | 5 min |

**2 BLOCKER / 0 MAJOR / 1 MINOR**

## PASSE 7 — Figures et tableaux

| ID | Sév. | Emplacement | Constat | Preuve | Correctif | Effort |
|---|---|---|---|---|---|---|
| P7-01 | MAJOR | `fig:compounding` | $B_1$ (red, solid) and $M$ (green, solid) — the two most important curves to distinguish — differ **only** by color (both solid lines); red/green is the classic colorblind-confusable pair, and both would be indistinguishable in grayscale print | TikZ source, L465-468 | Give $B_1$ a distinct dash/marker | 15 min |
| P7-04 | MINOR | `fig:pipeline` | Light 8%-tint color fills (red/green) for semantic distinction may not print visibly in grayscale; text labels remain legible regardless | TikZ source | Low priority given labels compensate | — |
| — | checked | — | All figures/tables referenced near point of use; captions self-contained; no truncated/misleading axes | Full read | — | — |

**0 BLOCKER / 1 MAJOR / 1 MINOR**

## PASSE 8 — Bibliographie et positionnement

| ID | Sév. | Emplacement | Constat | Preuve | Correctif | Effort |
|---|---|---|---|---|---|---|
| P8-01 | MAJOR | L106, L350 | GridCraft (primary experimental environment, ~10+ mentions) is never cited, despite `references.bib` already containing a ready, anonymized entry (`gridcraft2026anonymous`) for exactly this purpose | `grep gridcraft2026anonymous references.bib` (present, unused); `grep GridCraft paper.tex` (no `\citep` anywhere) | Add `~\citep{gridcraft2026anonymous}` at first mention | 2 min |
| P8-03 | QUESTION | `references.bib` (107 entries) | Spot-checked the 3 most fabrication-risk-prone (2025/2026-dated) citations — Athalye et al. 2026, Lillemark et al. 2026, WALL-E/2.0 — all verified real via live web search. Did **not** re-verify all 107 entries individually; this project has a documented history (this session's memory) of previously-fixed fabricated citations, so a final full pass is recommended. | Web searches (3/3 confirmed) | Full bib audit if time permits | 1-2h |
| — | checked | — | 0 cited-but-missing keys, 0 undefined references in build log; ~68 unused bib entries (harmless clutter from prior drafts) | scripted diff, `paper.log` | — | — |

**0 BLOCKER / 1 MAJOR**

## PASSE 9 — Écriture et lisibilité

| ID | Sév. | Emplacement | Constat | Preuve | Correctif | Effort |
|---|---|---|---|---|---|---|
| P9-01 | MINOR | §5 discussion paragraphs (e.g. L267, L291, L297, L339) | Several 60-95-word, multi-clause sentences; correct but dense, likely to cost clarity points with a fast/non-specialist reviewer | Word counts | Split into 2 sentences each | 20 min |
| — | checked | — | Acronyms defined at first use; no obvious non-native-English artifacts; chktex nits are cosmetic (space-before-label, missing braces around a citation parenthetical) and not real AAAI-compliance issues | `chktex`, `lacheck`, full read | — | — |

**0 BLOCKER/MAJOR / 1 MINOR**

## PASSE 10 — Simulation adversariale de relecture

**R1 — sub-domain expert, novelty-skeptical.**
Strengths: the 5.5→5.6→5.7 triptych is a genuine theoretical story; the
non-identifiability result is non-obvious. Weaknesses: the paper's own
canonical spatial-invariant example is conceded (L115) to be an instance of
Flow-Equivariant World Models' (Lillemark et al. 2026) equivariance class —
no experiment isolates what the discovery+certification protocol adds beyond
that prior characterization, or beyond ConCerNet/IAEM's existing
residual/contrastive schemes; the uncited "our prior NS-MAWM framework"
language makes it hard to tell what is actually new here.
*Score: borderline, leaning reject — novelty argued, not measured.*

**R2 — empiricist, statistics-focused.**
Strengths: unusually honest uncertainty reporting for a synthetic dataset.
Weaknesses (severe): the transfer table's own significance claim is
arithmetically wrong (P5-01); $n=5$ seeds, by the paper's own power
calculation, supports almost nothing beyond "P1 is worse than P2/P3"; zero
baseline comparison (self-admitted); zero code, logs, or data to check any
number against.
*Score: reject. Self-awareness of statistical limits is not evidence.*

**R3 — non-specialist, clarity/motivation-focused.**
Strengths: page-1 motivating question is sharp and well-posed.
Weaknesses: "five results" (abstract) vs. what Section 5 visibly contains is
confusing on a first read (P3-02); "our own prior work"/"our prior NS-MAWM
framework" reads strangely in what is supposed to be an anonymous
submission — confusing regardless of the anonymity question itself; several
intro sentences require re-reading.
*Score: weak accept on motivation alone; the self-citation framing actively
confused me.*

**Motif de rejet le plus probable, en une phrase :** desk-reject sur la
conformité (dépassement de pages + checklist de reproductibilité vide) avant
même l'examen scientifique ; si évité, rejet substantif pour absence de
toute donnée réelle et de comparaison à une baseline.

**Le maillon faible unique :** l'absence totale de code/données réelles —
tout le tableau expérimental est une valeur inventée, honnêtement documentée
comme telle, mais une valeur inventée reste une valeur inventée face à un
relecteur.

**Les 3 questions de rebuttal sans réponse aujourd'hui :**
1. "Logs seed-par-seed des Tableaux 2–6 ?" → inexistants ; nécessite
   d'implémenter P1/P2/P3 + F1–F4 (`TODO-EXPERIMENTS.md` #1–2).
2. "Comparaison à WALL-E/SAM ?" → nécessite d'implémenter la baseline
   heuristique (`TODO-EXPERIMENTS.md` #5).
3. "Le gain P2 vs P3 sur SMACv2 est-il robuste ?" → non, ni statistiquement
   (5 seeds, ~47 nécessaires) ni même arithmétiquement (P5-01: la valeur
   rapportée est fausse).

**Verdict méta : reject probable tel que soumis** (distance au seuil :
loin, à cause du blocage de conformité) ; **en supposant la conformité
corrigée : borderline-reject sur le fond** (théorie solide et honnêtement
présentée, zéro donnée réelle).

## PASSE 11 — Éthique, impact, LLM

| ID | Sév. | Emplacement | Constat | Preuve | Correctif | Effort |
|---|---|---|---|---|---|---|
| P11-01 | QUESTION | Whole doc | No ethics/broader-impact statement; likely not required (no human subjects, no dual-use concern visible), but AAAI's Code of Professional Conduct expectations are broader than this one optional statement | grep, full read | Judgment call for authors | — |
| P11-04 | NON VÉRIFIABLE | — | Conflicts of interest, LLM-disclosure portal checkbox | Submission-system-level, not visible from files | Verify directly on the AAAI-27 submission portal | — |
| — | checked | — | No human-subjects data; all environments are standard synthetic RL benchmarks | Full read | — | — |

**0 BLOCKER / 0 MAJOR / 2 QUESTION/NON VÉRIFIABLE**

## PASSE 12 — Porte finale

See `BLOCKERS.md` for the full blocking list (6 items: P1-01, P2-01, P2-02,
P5-01, P6-01, P6-02).

**Plan d'action, par ratio impact/effort :**
- *Dans les 2h :* P8-01 (cite GridCraft, 2 min) · P3-01 ("looser"→"tighter",
  2 min) · P5-01 (fix t-value + prose, 30 min) · P7-01 (distinguish curves,
  15 min) · P2-01/P2-02 rewrite (30-60 min, **highest priority given
  desk-reject risk**) · P6-01 (fill checklist honestly, 1-2h).
- *Aujourd'hui, avant la deadline :* apply `PAGE-BUDGET.md`'s cut sequence
  1–5 **and** trim §3/§4.2 as it recommends — cuts 1–5 alone save only
  ~1.3–1.5 pages, not enough to reach 9 total from 12.
- *Si le temps le permet :* full 107-entry bib audit (P8-03) · mention
  Theorem 5.7 in abstract/intro (P3-02) · sentence-splitting (P9-01).

**Checklist opérationnelle :** main PDF (after page cuts) · supplementary
PDF (already compliant, separate, unlimited) · Reproducibility Checklist PDF
(must be regenerated after P6-01) · no code/data archive — state why
explicitly in the checklist rather than omitting silently · keywords
already present · conflicts of interest (portal-level, verify separately) ·
re-verify the exact UTC-12 cutoff against your local timezone before final
upload.

**Verdict final : NE PAS SOUMETTRE EN L'ÉTAT.** All 6 blockers in
`BLOCKERS.md` must clear, and the page count must be *actually* reduced to
9 (not merely documented as over-budget) before upload.
