# Reviewer Vocabulary and Wording Corrections

This document consolidates vocabulary, phrasing, notation, and style issues explicitly raised or implied by the ICML and JFSMA reviews. It is meant as a correction checklist for the NeurIPS version.

Applied pass on 2026-04-19:
- removed the remaining high-risk terms `determinable`, `undeterminable`, `ambiguous transitions`, `parametric mapping`, `Under suitable assumptions`, and `Our framework...`;
- softened several empirical claims so that prediction, planning/control, robustness, OOD behavior, and data-limited learning are framed as evidence-tested claims rather than guaranteed outcomes;
- clarified open-loop rollouts, one-hot feature representation, variational-inference citations, and evaluation-section orientation;
- cleaned a targeted subset of bibliography metadata, including `OpenReview.net` publisher noise, the Garcez citation key, and several protected benchmark/acronym names.

Status labels:
- `addressed`: the current NeurIPS draft already appears to handle the issue.
- `partial`: the current draft mostly handles the issue, but a local wording or consistency pass is still useful.
- `to fix`: the issue should still be corrected in the NeurIPS draft or bibliography.

## A. High-priority terminology affecting the scientific claim

| ID | Source | Element to correct | Problem | Suggested correction | Status |
|---|---|---|---|---|---|
| V1 | ICML EPKz, ICML YgDJ | "determinable features", "undeterminable features" | Reviewers found the term ambiguous and non-standard. It can suggest determinism rather than symbolic coverage. | Use "symbolically predictable features" for features whose next value can be inferred from symbolic rules, and "residual features" or "uncovered features" for the rest. Define both through the coverage mask. | addressed |
| V2 | ICML qGB8, ICML YgDJ, ICML Nx4Y | Claims about "planning/control improvements" | The previous wording claimed planning/control benefits while the evidence mainly concerned prediction metrics. This creates an overclaim. | Use conditional/evidence-aligned wording: "we evaluate downstream planning/control", "we test whether semantically reliable rollouts improve decision quality". Only write "improves" once final downstream results support it. | partial |
| V3 | ICML YgDJ, ICML Nx4Y, JFSMA | "RVR = 0" presented as a performance result | For projection and residual modes, zero post-correction RVR is partly built into the method and should not be framed as learned superiority. | Write: "For projection and residual modes, RVR_post=0 on covered features under correct rules and masks by construction." Report RVR_pre and correction magnitude to measure learned coherence and intervention size. | addressed |
| V4 | ICML EPKz, ICML qGB8 | "handcrafted task-specific rules" | Reviewers worried that symbolic rules are comparable to reward engineering and may harm scalability. | Use "domain transition rules", "domain invariants", or "symbolic transition knowledge". Add the distinction: rewards specify preferences, while symbolic rules constrain plausible transitions. Acknowledge rule-authoring effort. | addressed |
| V5 | JFSMA, ICML | "contribution" applied to protocol, RVR, code, hyperparameters, rules | This dilutes the paper. The user also clarified that NS-MAWM is the single contribution. | State that NS-MAWM is the contribution. Treat metrics, protocol, code, rule inventory, hyperparameters, and checklist items as validation and reproducibility apparatus. | addressed |
| V6 | JFSMA | "regularisation de coherence" potentially confused with reward shaping | The phrase can make the symbolic penalty look like a reward-design trick. | Use "symbolic consistency regularization" and define it as an auxiliary training loss over covered features, not as a reward modification. | addressed |
| V7 | JFSMA | "ambiguous features" | A reviewer asks whether "ambiguous" means stochastic, non-deterministic, residual, or undefined. | Prefer "residual", "uncovered", "stochastic", or "high-entropy" depending on the exact meaning. If "ambiguous" remains, define it explicitly. Recommended replacement: "uncovered or high-entropy transitions". | addressed |
| V8 | ICML | "neurosymbolic" vs "neuro-symbolic" | Inconsistent spelling weakens polish. | Use "neuro-symbolic" consistently in prose. Keep "Neuro-Symbolic Multi-Agent World Models" for the full name. Preserve spelling only inside cited titles if needed. | addressed |

## B. Formal vocabulary, notation, and definitions

| ID | Source | Element to correct | Problem | Suggested correction | Status |
|---|---|---|---|---|---|
| N1 | ICML qGB8, JFSMA | Undefined `Omega`, `A`, action spaces | Reviewers flagged notation introduced without definition. | Define observation spaces, action spaces, joint observation, joint action, transition, reward, and history before use. Keep a notation table. | addressed |
| N2 | JFSMA | `Delta(A)` | Probability simplex notation was not explained. | Define `Delta(A)` as the set of probability distributions over action space `A`. | addressed |
| N3 | JFSMA | `omega` and joint observation notation | Some symbols were difficult for non-MARL readers. | Define `omega_t^i` as agent `i`'s local observation, `omega_t^j` as the joint observation, and state that superscript `j` means joint, not an agent index. | addressed |
| N4 | JFSMA | `a_t`, `a_i`, agent/time index conflicts | The old notation could confuse time indices and agent indices. | Use `a_t^i` for action of agent `i` at time `t`, and `a_t^j` for joint action. Avoid `a_x` unless `x` is explicitly an agent index. | addressed |
| N5 | JFSMA | `f^k`, feature notation | Feature index notation was unclear or undefined. | Define feature set `F`, feature index `k`, and feature values `f_{t,k}^i` or avoid feature-level notation when masks suffice. | addressed |
| N6 | JFSMA | `concat`, `flatten`, `unflatten`, long matrix formulae | The formulae were hard to read and not reused enough to justify complexity. | Replace long expressions with compact operators, or move implementation-level tensor reshaping to appendix/pseudocode. Use prose plus one clean equation. | partial |
| N7 | JFSMA | Figure notation `u` and `d` | Reviewer found `u`/`d` confusing in the method figure. | Label figure components directly as "covered/symbolic" and "residual/neural"; avoid relying on one-letter labels. | addressed |
| N8 | JFSMA | `w^reg`, `omega^reg`, predicted symbols | A reviewer noted a notation appearing without introduction. | Introduce each prediction variant before use: pre, regularized, projected, residual, post. Keep naming consistent with `RVR_pre` and `RVR_post`. | addressed |
| N9 | ICML Nx4Y | Formal guarantees and RVR | Reviewer asked whether RVR can be analyzed or proven. | State only the conditional guarantee on covered features. Frame RVR as an empirical violation-probability estimate, not a global correctness certificate. | addressed |
| N10 | JFSMA | "hypotheses appropriees" / "under suitable assumptions" | This is too vague for readers outside MARL. | Replace with concrete wording, e.g. "under assumptions such as bounded rewards, sufficient model accuracy, and a planning procedure robust to compounding model error". Add references if needed. | addressed |
| N11 | JFSMA | "invariants and equivariances" | The terms may not be clear to non-specialists. | Add a short definition: invariants are features that should remain unchanged under an action; equivariances are predictable transformations induced by actions or coordinate changes. | partial |
| N12 | JFSMA | "soft constraint", "hard constraint" | Potentially unclear if not tied to inference behavior. | Define: a soft constraint is penalized during training but may be violated at inference; a hard constraint overwrites or constructs covered outputs so they satisfy rules under correct masks/rules. | addressed |

## C. Claims, epistemic status, and hedging

| ID | Source | Element to correct | Problem | Suggested correction | Status |
|---|---|---|---|---|---|
| C1 | ICML YgDJ | "superior symbolic coherence" | Too strong if the headline metric is enforced by construction. | Write "final covered-feature validity is enforced by construction"; reserve "learned coherence" for RVR_pre reductions. | addressed |
| C2 | ICML qGB8, ICML YgDJ | "better planning performance" | Unsupported unless downstream experiments are shown. | Use "decision relevance", "downstream planning/control evaluation", or "we test whether". In result paragraphs, tie claims to final returns, success rates, and invalid-plan rates. | partial |
| C3 | ICML Nx4Y | "symbolic rules improve generalization" | Needs OOD evidence and careful causality. | Write "we evaluate whether symbolic structure improves OOD robustness" until OOD results are final. | partial |
| C4 | ICML, JFSMA | "zero RVR" without scope | Can be mistaken for full rollout correctness. | Always qualify: zero RVR applies only to symbolically covered features, under correct rules and masks, and says nothing about residual or hidden variables. | addressed |
| C5 | JFSMA | "lightweight correction" | Reviewer asks how this is known. | Avoid "lightweight" unless runtime is measured. Use "post-correction layer" and report wall-clock/runtime or correction magnitude. | partial |
| C6 | ICML | "scalability" | Symbolic rules raise questions about rule authoring and increasing numbers of agents/rules. | Use measured wording: "scales to the evaluated settings"; put broader scalability under limitations and future work unless empirical scaling is included. | partial |
| C7 | JFSMA | "recent efforts" | Problematic when papers have the same year or the chronology is unclear. | Use "related efforts", "contemporary work", or "recent lines of work" only when the date relation is accurate. | to fix |

## D. English wording replacing French-version awkward phrasing

| ID | Source | Element to correct | Problem | Suggested correction | Status |
|---|---|---|---|---|---|
| W1 | JFSMA | "Ces erreurs se cumulent sur les rollouts degradent la planification" | Missing grammatical link. | "Such errors accumulate during open-loop rollouts and can degrade downstream planning." | addressed |
| W2 | JFSMA | Anglicisms: "rollout", "backbone", "benchmark", "layout" | In French these were criticized as anglicisms; in NeurIPS English they are acceptable but should be defined. | Define once: "open-loop rollout", "shared MAWM backbone", "benchmark environment", "environment layout". | partial |
| W3 | JFSMA | "efficacite en echantillons" | Awkward French. | In English use standard "sample efficiency"; if explaining, write "performance obtained from a fixed number of environment transitions". | addressed |
| W4 | JFSMA | "mappage" | Awkward French and too literal. | In English prefer "parametric function" or "mapping". In the NeurIPS draft, "parametric function" is cleaner than "parametric mapping". | addressed |
| W5 | JFSMA | "retour attendu" | Reviewer asks whether this means reward. | In English use "expected return" and define it as discounted cumulative reward under a policy. | addressed |
| W6 | JFSMA | "la paire encodeur-decodeur est typiquement implementee avec des architectures MLP ou a attention" | May sound too categorical. | "The encoder-decoder pair is typically implemented with MLPs and, in some variants, attention-based modules." | partial |
| W7 | JFSMA | "optimises avec Adam" | Reviewer asks "Who is Adam?" | "optimized with Adam~\\cite{kingma2017adammethodstochasticoptimization}" at first mention. | addressed |
| W8 | JFSMA | "problematique prolonge nos travaux" | Awkward wording. | "This work builds on prior work..." or "This paper extends prior work..." | to fix if still present |
| W9 | JFSMA | "plusieurs travaux ... [single citation]" | Mismatch between plural phrasing and one citation. | Either cite several works or use singular wording: "A prior work..." | to fix in final citation pass |
| W10 | JFSMA | "grande dimension" | French agreement issue. | In English write "high-dimensional observations". | addressed |
| W11 | JFSMA | "comme un LSTM" | Slightly informal. | "such as an LSTM" or "for example, an LSTM". | addressed |
| W12 | JFSMA | "ambigues" | Reviewer asks "ambiguous = non-deterministic?" | Replace with "stochastic", "uncovered", "residual", or "high-entropy" depending on the intended meaning. | partial |
| W13 | JFSMA | "rejouement" | Potentially non-standard. | In English use "replay buffer"; in French use "rejeu" if needed. | addressed |
| W14 | JFSMA | "base sur" | French style issue. | In English "LSTM-based" is acceptable; in French use "fonde sur". | not relevant to English draft |
| W15 | JFSMA | "encodees" for one-hot values | Could be confused with neural encoder. | "represented as one-hot vectors" or "one-hot encoded categorical features". | addressed |

## E. Organization and readability phrasing

| ID | Source | Element to correct | Problem | Suggested correction | Status |
|---|---|---|---|---|---|
| O1 | JFSMA | Too many semicolons and punctuation in inline lists | Reviewers found punctuation heavy and visually noisy. | Convert long inline lists into bullets, or use commas and one final conjunction. Avoid period-plus-semicolon sequences. | partial |
| O2 | JFSMA | Section immediately followed by subsection | Reviewer suggests a short chapeau before subsections. | Add one orienting sentence after major section titles before the first subsection, especially Background and Evaluation. | partial |
| O3 | JFSMA | Excessive backward/forward subsection references | Too many "(Subsection X.Y)" references interrupt reading. | Keep references only when needed for navigation. Prefer natural prose: "The next paragraph defines..." or omit if nearby. | partial |
| O4 | JFSMA | Bold full paper titles or environment names inconsistently | Looks visually inconsistent and non-standard. | Use method names or short citations in normal text. Bold only deliberate terms at first definition. Homogenize environment names. | partial |
| O5 | ICML/JFSMA | "G" notation confusion | JFSMA reviewer expected "V" for verrou, while NeurIPS uses gaps. | In English NeurIPS draft, explicitly define "G1-G3 are gaps". Do not use `G` for goals. | addressed |
| O6 | JFSMA | Long formula before figure and delayed figure reference | Reader cannot connect prose, formulas, and figure. | Introduce the figure near first methodological overview and reference it where each component is explained. | partial |
| O7 | JFSMA | Captions and tables not self-contained enough | Reviewers wanted clearer figure/table semantics. | Make captions explain what each color/component/metric means, especially covered vs residual and RVR_pre vs RVR_post. | partial |

## F. Environment names, acronyms, and benchmark vocabulary

| ID | Source | Element to correct | Problem | Suggested correction | Status |
|---|---|---|---|---|---|
| A1 | ICML Nx4Y, JFSMA | "SMAC" | Reviewer specifically says it should be SMACv2 in the evaluated benchmark. | First mention: "StarCraft Multi-Agent Challenge v2 (SMACv2)"; afterwards use "SMACv2". | addressed |
| A2 | JFSMA | MARL, MBRL, MB-MARL | Acronyms need consistent capitalization and first-use expansion. | First use: "multi-agent reinforcement learning (MARL)", "model-based reinforcement learning (MBRL)", "model-based MARL (MB-MARL)". Protect acronyms in BibTeX titles. | partial |
| A3 | JFSMA | MOISE+ / MOISE / moise+ | Bibliography capitalization issue. | Use the official capitalization and protect it in BibTeX, e.g. `{MOISE+}` if present in titles. | to fix in bibliography audit |
| A4 | JFSMA | "benchmark" | In French version criticized as anglicism; in English it is standard. | Use "benchmark environment" or "benchmark suite" when the meaning is an environment, not an experimental comparison. | partial |
| A5 | JFSMA | "layout" | In French version criticized as anglicism; in English it is standard but should be concrete. | Use "environment layout", "map layout", or "Overcooked layout" depending on context. | partial |

## G. Bibliography and citation wording

| ID | Source | Element to correct | Problem | Suggested correction | Status |
|---|---|---|---|---|---|
| B1 | JFSMA | References incomplete | Reviewer says many entries miss authors, venue, or official metadata. | Audit `references.bib` against DBLP/publisher/OpenReview official entries. Fill authors, year, venue, pages/URL/DOI where applicable. | to fix |
| B2 | JFSMA | Lowercase acronyms in BibTeX titles | Acronyms such as MARL, SMAC, MBRL, MOISE+ can be downcased by BibTeX. | Protect acronyms with braces: `{MARL}`, `{SMACv2}`, `{MBRL}`, `{MOISE+}`, `{Dec-POMDP}`. | to fix |
| B3 | JFSMA | "OpenReview.net" metadata noise | Reviewer says this information is not useful in references. | For OpenReview papers, keep the venue and URL where appropriate, but avoid noisy publisher fields that print "OpenReview.net" unnecessarily. | addressed |
| B4 | JFSMA | Citations glued to text, e.g. `MB-MARL[` | Missing spacing before citations harms polish. | Use non-breaking citation spacing consistently: `MB-MARL~\\cite{...}`. | partial |
| B5 | JFSMA | Semantic loss and differentiable logic citations | The wording should make clear whether these are examples, not the same method. | "such as semantic loss and differentiable logical rules" with citations. | addressed |
| B6 | JFSMA | Variational inference claim without citation | If the background says WMs use variational inference, the source should be nearby. | Cite PlaNet/Dreamer or the relevant WM source in the same sentence. | addressed |

## H. Concrete local edits suggested for the current NeurIPS draft

These are small wording edits still worth applying during the next article pass.

| ID | Current pattern | Suggested edit | Reason |
|---|---|---|---|
| L1 | "ambiguous or high-entropy transitions" | "uncovered or high-entropy transitions" | Avoids the reviewer-triggering ambiguity around "ambiguous". |
| L2 | "parametric mapping" | "parametric function" | Cleaner academic wording. |
| L3 | "Under suitable assumptions" | Specify representative assumptions or cite them. | Avoids vague background phrasing. |
| L4 | "Our framework NS-MAWM builds..." | "NS-MAWM builds..." | Tighter and less self-referential. |
| L5 | "planning/control improves" style sentences | Keep "tests whether" unless final downstream results are inserted. | Prevents overclaiming. |
| L6 | "recent efforts" | "related efforts" or "contemporary work" | Avoids chronological overprecision. |
| L7 | Bibliography acronyms | Brace acronyms in titles. | Prevents lowercasing in final PDF. |
| L8 | Background sections with immediate subsections | Add one chapeau sentence. | Matches reviewer readability request and NeurIPS polish. |

## I. Recommended replacement lexicon

Use this vocabulary consistently across abstract, introduction, method, evaluation, tables, and captions.

| Avoid or limit | Prefer |
|---|---|
| determinable features | symbolically predictable features, covered features |
| undeterminable features | residual features, uncovered features |
| ambiguous features | residual, stochastic, uncovered, or high-entropy features |
| null RVR | zero RVR, `RVR=0`, `RVR_post=0` |
| zero RVR as result | zero post-correction RVR by construction on covered features |
| handcrafted rules | domain transition rules, domain invariants, symbolic transition knowledge |
| reward shaping | symbolic consistency regularization, auxiliary consistency loss |
| planning/control improvement | downstream planning/control evaluation, decision relevance |
| proves improved return | empirically tests improved return |
| semantic guarantee | covered-feature guarantee under correct rules and masks |
| global correctness | semantic validity on covered features plus empirical residual evaluation |
| lightweight correction | post-correction layer, correction magnitude, runtime overhead |
| SMAC | SMACv2 |
| neurosymbolic | neuro-symbolic |
