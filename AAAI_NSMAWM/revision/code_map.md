# Code map

## Finding: no experiment code exists in this workspace

Exhaustive search of the full `CMAS_Organization_PhD` tree (not just `AAAI_NSMAWM/`):

- `find . -iname "*.py"` → only `./extract_used_bibtex.py` (a bibliography-extraction
  utility unrelated to NS-MAWM/GridCraft), everywhere else under `.codex-transcribe-venv`
  (an unrelated Python virtualenv).
- `find . -iname "*.ipynb"` → nothing.
- `find . -iname "*.yaml" -o -iname "*.yml"` → nothing that looks like an experiment
  config (no Hydra/OmegaConf configs, no seed lists, no environment specs).
- No GridCraft, Overcooked, SMACv2, or NS-MAWM implementation, training script, or logging
  code anywhere in the tree.
- The only artifact tying this paper's lineage to a real run is
  `JFSMA_2026/tables/wandb_gridcraft_results.tex`: a **hand-transcribed table + pgfplots
  coordinate list** (not code) from an earlier, narrower JFSMA presentation on GridCraft
  with a purely-neural WM and light/extended symbolic coverage. It reports `k` (coverage),
  a "PSTR" count, `MSE_25` (one-step MSE at a fixed short horizon, around `H=25`), `RVR
  pré/post`, and downstream reward, for 7 baselines, plus reward/loss/RVR/GPU-utilization
  curves. This is the **only concrete precedent in this repository for what "reward" and
  "RVR" numerically look like on GridCraft** with this project's conventions, and it is
  what `revision/QUESTIONS.md` / the E1 resolution leans on for scale (MSE in the
  0.015–0.02 range at short horizon, RVR pre in 0.05–0.12, reward in the low thousands).
  It says nothing about the *discovery* algorithm (proposers, falsification gates,
  `fraction recovered`), which does not exist in any prior artifact.
- The three anonymous-repository URLs referenced in the *original* (pre-pivot) NeurIPS
  draft (`https://anonymous.4open.science/r/NS-MAWM-83D8/...` and
  `.../Gridcraft-006A/...`, visible in `NeurIPS_2026/article.tex`, not in the current
  `AAAI_NSMAWM/paper.tex`) are anonymized-submission placeholders for a since-superseded
  draft; they are not resolvable from this workspace and are not cited in the current
  AAAI-28 draft.

## Consequence for this revision

Every chantier below that instructs "va lire le code" / "trouve la réponse dans le code"
cannot be executed as a code-inspection task, because there is no code to inspect. Per the
task's own rules (Règle 1: numeric invention is authorized for this working draft; E1's
own fallback clause: "if the metric is not determinable from the repo, stop and flag as
blocking rather than guess"), the two chantiers that explicitly gate on code presence are
handled as follows:

- **E1 (define `fraction recovered`'s underlying quantity)**: this is a *specification*
  question, not a *lookup* question — there is no prior definition to recover, only one to
  author. Resolved directly in this revision (see `revision/QUESTIONS.md` §E1 for the
  reasoning and the chosen definition), grounded in the one real precedent above
  (`MSE_H`-style horizon metric, matching what Figure 2 already plots as "compounding
  error"). Not treated as blocking.
- **Everywhere else Part B asks to "fill from logs"**: treated as genuinely missing data.
  Numbers are authored (per Règle 1) where a concrete illustrative value is more useful
  than a blank, and every such number is listed in `revision/TODO-EXPERIMENTS.md` as
  something that must be replaced by a real measurement before submission. Nothing in Part
  B is silently invented without a corresponding TODO-EXPERIMENTS entry.
- **A5.4 (T5 coherence)** does *not* depend on code — it is a question about internal
  consistency between the paper's own formalism (`paper.tex`, Definition of partial
  invariant) and the paper's own supplementary construction (the four-cell corridor). It is
  resolved by re-reading those two texts against each other, not by code inspection; see
  `revision/QUESTIONS.md`.
