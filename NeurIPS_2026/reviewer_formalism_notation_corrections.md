# Reviewer Formalism and Notation Corrections

This document consolidates reviewer remarks about mathematical formalism, notation, equations, proof status, and formal phrasing in the ICML and JFSMA reviews. It complements `reviewer_vocabulary_corrections.md`, which focuses on terminology and prose.

Applied formalism pass on 2026-04-19:
- separated joint histories `h_t^j` from recurrent hidden states `\tilde h_t^j`;
- removed the nested MAWM equation with `flatten/unflatten/concat` from the main formalism and replaced it with numbered encode/update/decode equations;
- introduced covered/residual selection and insertion operators `P_d`, `P_u`, `\iota_d`, and `\iota_u`;
- rewrote symbolic projection, residual assembly, RVR, correction magnitude, and the formal propositions using these operators;
- changed feature notation to `f_{t,k}^i` and added labels for the core equations.

Status labels:
- `addressed`: already mostly handled in the current NeurIPS draft.
- `partial`: partly handled, but still worth correcting or tightening.
- `to fix`: should be corrected in the next formalism pass.

## A. Global Formalization and Notation Hygiene

| ID | Source | Element to correct | Problem identified by reviewers | Suggested correction | Current status |
|---|---|---|---|---|---|
| F1 | JFSMA R2 | Global mathematical formalization | The formalization was judged useful but inconsistent: undefined variables, index errors, dimension mismatches, and formulas that are too hard to read. | Maintain one notation table early; introduce every symbol before use; avoid one-off heavy notation; make the method equations follow the same symbol conventions as the background. | addressed |
| F2 | JFSMA R2 | Agent/time index convention | The old version mixed `a_x` where `x` meant agent and `a_t` where `t` meant time. | Use superscript for agent index and subscript for time: `a_t^i`, `\omega_t^i`; use superscript `j` only for joint quantities. State explicitly that `j` is not an agent index. | addressed |
| F3 | JFSMA R2 | Undefined `j` in `T_\theta^j`, `\omega_t^j` | Reviewer did not know what `j` meant. | In the notation table: `\omega_t^j`, `a_t^j`, `h_t^j` are joint quantities. Avoid `j` as a free index. | addressed |
| F4 | JFSMA R2 | Index bases `0 <= k` vs first feature `f_{1,t}` | Inconsistent indexing can imply `n_f+1` features. | Use `1 \leq k \leq n_f` for feature indices and `1 \leq i \leq n` for agents. Time may start at `t=0`. Avoid mixing 0-based and 1-based feature indices. | addressed |
| F5 | JFSMA R2 | Missing indices on `\omega_t^d`, `\omega_t^u` | Reviewer noted that agent index disappeared in some decompositions. | Use local components as `\omega_t^{d,i}`, `\omega_t^{u,i}` and joint components as `\omega_t^{d,j}`, `\omega_t^{u,j}`. Do not use unindexed `\omega_t^d` unless explicitly global. | addressed |
| F6 | JFSMA R2 | Multiple notational forms for joint objects | Reviewer found `\pi^j=(...)` vs `H_joint=H_1\times...` heterogeneous. | Prefer consistent notation: `\pi^j=(\pi_1,\ldots,\pi_n)`, `A^j=A_1\times\cdots\times A_n`, `\Omega^j=\Omega_1\times\cdots\times\Omega_n`, and `H^j=H_1\times\cdots\times H_n`. | addressed |
| F7 | JFSMA R2 | Repeated use of `joint` as text and `j` as superscript | Can increase notation burden. | Define all joint spaces once, then use `^j` consistently. Add one sentence: "Superscript `j` abbreviates joint and is not an exponent." | addressed |
| F8 | JFSMA R2, ICML qGB8 | Undefined `\Omega`, `A`, action/observation spaces | ICML explicitly flagged missing definitions of `\Omega` and `A`. | Define `\Omega_i`, `A_i`, `\Omega^j`, `A^j`, and the joint action/observation spaces before policies and histories. | addressed |

## B. Background Formalism

| ID | Source | Element to correct | Problem identified by reviewers | Suggested correction | Current status |
|---|---|---|---|---|---|
| B1 | JFSMA R2 | `\Delta(A)` | Reviewer asked what `\Delta` means. | Define `\Delta(A_i)` as the probability simplex over actions in `A_i`. | addressed |
| B2 | JFSMA R2 | `\omega` | Reviewer asked what `\omega` means. | Define `\omega_t^i` as local observation and `\omega_t^j` as joint observation before history notation. | addressed |
| B3 | JFSMA R2 | Expected return vs reward | Reviewer asked whether "retour attendu" means reward. | Use "expected return" and define it as expected discounted cumulative reward. Keep reward as `R`. | addressed |
| B4 | JFSMA R2 | Finite/infinite horizon phrase | The phrase "finite horizon `T` or infinite horizon and `\gamma < 1`" had two possible readings. | Write: "finite horizon `T`; for the infinite-horizon case, assume `\gamma<1` and take `T\rightarrow\infty`." | addressed |
| B5 | JFSMA R2 | Discount factor intuition | Reviewer questioned `\gamma^t` because later rewards get smaller. | Add or keep a concise explanation that this is the standard discounted-return convention; if needed, say it weights near-term rewards more strongly in infinite-horizon objectives. | addressed |
| B6 | JFSMA R2 | `\hat P_\phi`, `\hat R_\phi` | Reviewer said these predictors were not defined. | Define `\hat P_\phi` as learned transition predictor and `\hat R_\phi` as learned reward predictor before use. | addressed |
| B7 | JFSMA R2 | "under suitable assumptions" | Too vague for non-MARL readers. | Replace with concrete representative assumptions: bounded rewards, sufficient model accuracy, and a planner robust to compounding model error. Add citations. | addressed |
| B8 | JFSMA R2 | Variational inference claim | Reviewer asked for a reference. | Cite PlaNet/Dreamer near the sentence. | addressed |
| B9 | JFSMA R2 | RNN hidden state introduced before `\mathcal H` | The original order introduced recurrent hidden state before defining the history/hidden-state space. | Introduce `\mathcal H` and histories before using `\tilde h_t`, or explicitly define `\mathcal H` in the WM subsection before the formula. | addressed |
| B10 | JFSMA R2 | Too dense Dec-POMDP definition | Reviewer suggested itemizing definitions. | Convert the Dec-POMDP tuple explanation into a clean aligned list or keep semicolon-separated definitions but ensure readability. | partial |

## C. World-Model and MAWM Equations

| ID | Source | Element to correct | Problem identified by reviewers | Suggested correction | Current status |
|---|---|---|---|---|---|
| W1 | JFSMA R2 | Formula for `\mathcal T_\theta^j` | Reviewer found the formula unreadable and too long. | Replace the large nested `unflatten(Dec(f(concat(...))))` expression with a compact three-line system: encode, recurrent update, decode. Move `flatten/unflatten` details to prose or appendix. | addressed |
| W2 | JFSMA R2 | `concat`, `flatten`, `unflatten` | These operators make formulas hard to read and are implementation-level. | Define compact operators once, e.g. `\operatorname{vec}` for flattening and `\oplus` for concatenation, or omit them from main equations. | addressed |
| W3 | JFSMA R2 | Repetition between WM and MAWM sections | Reviewer noted repeated formulas and explanations. | Use the WM subsection for generic single-agent notation, then define MAWM as its joint-observation extension without repeating the full architecture twice. | addressed |
| W4 | JFSMA R2 | `h_t` vs `\tilde h_t` vs `h_t^j` | Reviewer noticed different hidden/history symbols. | Reserve `h_t^j` for interaction history and `\tilde h_t^j` for recurrent hidden state. State this explicitly in the notation table. | addressed |
| W5 | JFSMA R2 | `\mathcal H` ambiguity | `\mathcal H` may denote history space or recurrent hidden-state space. | Use `\mathbb H^j` or `\mathcal H^j` for histories and `\mathcal Z_h` or `\mathcal S_h` for recurrent hidden states. Avoid one symbol for both. | addressed |
| W6 | JFSMA R2 | Architecture mismatch in residual mode | Reviewer correctly noted that residual prediction has a smaller input/target space, so it is not the same neural architecture as full prediction. | Explicitly define `\mathcal T_\theta^{u,j}: \mathcal H^j \times \Omega^{u,j} \times A^j \to \Omega^{u,j}` as a distinct residual-output predictor with its own input/decoder dimensionality. | addressed |
| W7 | JFSMA R2 | `T_\theta` loses superscript `j` | Some equations dropped the joint superscript. | Use `\mathcal T_\theta^j` for full joint prediction and `\mathcal T_\theta^{u,j}` for residual prediction everywhere. | addressed |
| W8 | JFSMA R2 | Formula output equality confusion | Reviewer objected to equations that make raw neural output equal to final projected output. | Distinguish `\hat\omega^{pre,j}_{t+1}` from `\hat\omega^{proj,j}_{t+1}` and `\hat\omega^{post,j}_{t+1}`. Raw prediction is never equal by definition to projected/final output. | addressed |

## D. Structured Observation and Feature Decomposition

| ID | Source | Element to correct | Problem identified by reviewers | Suggested correction | Current status |
|---|---|---|---|---|---|
| S1 | JFSMA R2 | `f_{1,t}, f_{2,t}` notation | The repeated commas in indices and lists reduce readability. | Prefer `\omega_t^i=(f_{t,1}^i,\ldots,f_{t,n_f}^i)` or `f_{t,k}^i`; time before feature index is more standard in sequence modeling. | addressed |
| S2 | JFSMA R2 | Covered/residual decomposition readability | Reviewer suggested splitting into simpler equations. | Use: `\omega_t^i=\omega_t^{d,i}\oplus\omega_t^{u,i}`, `\omega_t^{d,i}=M_d^i\odot\omega_t^i`, `\omega_t^{u,i}=(1-M_d^i)\odot\omega_t^i` if the mask view is desired. | addressed |
| S3 | JFSMA R2 | Matrix notation used only once | Heavy matrix notation was introduced but not reused. | Remove the matrix formulation from the main text unless it is reused later; keep the feature-set/mask notation only. | addressed |
| S4 | JFSMA R2 | Dimension mismatch in projection equation | Reviewer saw mask matrices of one dimension multiplied with full vectors of another dimension. | Define `M_d` as the same shape as the decoded joint observation, or define projection operators `P_d` and `P_u` with explicit domains/codomains. | addressed |
| S5 | JFSMA R2 | `\oplus` concatenation | Reviewer suggested a dedicated concatenation operator. | Keep `\oplus` and define it once as feature concatenation. Use it consistently instead of bracket concatenation `[.,.]`. | addressed |
| S6 | JFSMA R2 | Covered feature rule notation `s(...)` | Needs exact domain and codomain. | Define each rule as `r_\ell: \mathcal H^j\times\Omega^j\times A^j\to \mathcal Y_\ell`, and define the symbolic transition operator as their aggregation. | addressed |
| S7 | ICML YgDJ | Number/fraction of symbolically handled features | Reviewer asked how many features are symbolic versus neural. | Define coverage ratio `\kappa=\|M_d\|_0/(n n_f)` and report actual values per environment. | partial |

## E. Integration Strategies and Figure Consistency

| ID | Source | Element to correct | Problem identified by reviewers | Suggested correction | Current status |
|---|---|---|---|---|---|
| I1 | JFSMA R2 | Figure 1 wrong/misleading symbols | Reviewer flagged possible wrong `\omega_t^j` vs `\omega_{t+1}^j` and incorrect arrows. | Ensure the method figure distinguishes input at time `t`, symbolic prediction for `t+1`, raw neural prediction for `t+1`, and final prediction for `t+1`. | addressed/verify visually |
| I2 | JFSMA R2 | Figure labels `u` and `d` | Reviewer found `u/d` misleading because boxes sometimes denote variables and sometimes components. | Label figure nodes as "covered symbolic component" and "residual neural component"; avoid isolated `u`/`d` boxes. | addressed/verify visually |
| I3 | JFSMA R2 | Missing references to figure subparts | Explanatory sections should point to corresponding figure parts. | When introducing regularization/projection/residual modes, reference the relevant panel in the method figure. | addressed |
| I4 | JFSMA R2 | Soft constraint phrase | Reviewer understood it but found it insufficiently formal for non-MARL readers. | Define soft constraint as an auxiliary penalty during training that can still be violated at inference. Define hard enforcement as projection/assembly that enforces covered features under correct rules/masks. | addressed |
| I5 | JFSMA R2 | `\hat\omega^{reg}` introduced without definition | Reviewer noted a new notation not introduced. | Define every prediction variant before its first equation: `pre`, `reg`, `proj`, `res`, `post`. | addressed |
| I6 | JFSMA R2 | Projection equation and dimensions | Reviewer saw a possible dimension error in `M_d \odot \omega^d + (1-M_d)\odot \hat\omega`. | Use full-sized embedded symbolic vector `\bar\omega^{d,j}_{t+1}` before masking, or define insertion operator `\iota_d`. Suggested equation: `\hat\omega^{proj,j}_{t+1}=\iota_d(\omega^{d,j}_{t+1})+\iota_u(P_u\hat\omega^{pre,j}_{t+1})`. | addressed |
| I7 | JFSMA R2 | Residual mode formula | Reviewer said all formulas must be rewritten if residual input is smaller. | Make residual mode formally separate: full predictor for reg/proj, residual predictor for res, with distinct target space and decoder. | addressed |
| I8 | JFSMA R2 | Post-correction purpose | Reviewer asked why post-correction exists if hard modes already enforce covered features. | State that post-correction is an ablation/diagnostic for neural and regularized baselines; it is redundant for projection/residual except for correction-magnitude analysis. | addressed |

## F. RVR, Statistics, and Guarantees

| ID | Source | Element to correct | Problem identified by reviewers | Suggested correction | Current status |
|---|---|---|---|---|---|
| R1 | ICML YgDJ, Nx4Y, JFSMA R3 | RVR zero by construction | Zero RVR for hard modes can be trivial and not comparable to learned coherence. | Split `RVR_pre` and `RVR_post`; report correction magnitude; state that `RVR_post=0` is a conditional guarantee on covered features, not learned behavior. | addressed |
| R2 | ICML Nx4Y | Statistical properties of RVR | Reviewer asked for analysis/proof of the RVR metric. | Define RVR as an empirical mean of Bernoulli violation indicators over covered agent-feature-time triples. State its expectation estimates violation probability under the evaluation distribution. Report mean/SE across seeds. | addressed |
| R3 | ICML Nx4Y | Theoretical analysis too weak | Reviewer asked for proof, convergence/error bounds, and drift analysis. | Add limited propositions only where true: covered-feature validity and covered/residual error decomposition. Explicitly state no universal convergence, drift, or return guarantee is claimed. | addressed |
| R4 | ICML Nx4Y | Long-horizon semantic drift not proven | Reviewer wanted proof symbolic constraints reduce drift. | Do not claim deductive proof of reduced drift unless available. Treat drift reduction as inductive and evaluate through horizon sweeps and RVR slope. | addressed |
| R5 | JFSMA R2 | RVR formula missing raw prediction context | Reviewer noted that `\omega_{t+1}^j` should be tied to `T_\theta(...)` before RVR. | Before defining RVR, restate which prediction is being evaluated: `\hat\omega^{pre,j}_{t+1}` for `RVR_pre` and `\hat\omega^{post,j}_{t+1}` for `RVR_post`. | addressed |
| R6 | JFSMA R2 | `RVR nul` phrasing | "Null" is misleading in math/CS. | Use `RVR=0`, `zero RVR`, or `\mathrm{RVR}_{post}=0`. | addressed |
| R7 | JFSMA R1/R2 | Missing uncertainty/significance | Results need error bars and significance interpretation. | Report mean ± standard error over seeds; specify number of seeds and what varies; use paired comparisons when methods share seeds/environments. | partial |
| R8 | JFSMA R2 | Correction magnitude | Needed to interpret hard RVR. | Define `\Delta_{\mathrm{corr}}` on covered positions and report it with RVR. | addressed |

## G. Equation Numbering and Cross-References

| ID | Source | Element to correct | Problem identified by reviewers | Suggested correction | Current status |
|---|---|---|---|---|---|
| X1 | JFSMA R2 | Equations not numbered | Reviewer could not refer to formulas. | Number only core equations: Dec-POMDP return, JOPM prediction, decomposition, symbolic transition, projection, residual assembly, RVR, correction magnitude, propositions. | addressed |
| X2 | JFSMA R2 | Too many subsection references | Reviewer found backward/forward subsection references heavy. | Keep formal references for figures, tables, algorithms, propositions, and distant equations. Remove obvious nearby subsection references. | partial |
| X3 | JFSMA R2 | Figure/formula references not aligned | Some figures were referenced too early and not used when needed. | Reference the method figure at the overview and again in each strategy paragraph. Keep references close to explanatory prose. | partial |
| X4 | JFSMA R2 | Section order | Background and method concepts were introduced in an order that made notation hard to follow. | Order should be: Dec-POMDP/MARL -> generic WM -> MAWM -> NS-MAWM problem -> NS-MAWM formalism -> strategies -> metrics/guarantees. | addressed |

## H. Concrete Corrections Recommended for the Current NeurIPS Draft

These are the most useful next edits to apply directly to `article.tex`.

| Priority | Current issue in NeurIPS draft | Recommended edit |
|---|---|---|
| Done | `\mathcal H` appeared to mean recurrent hidden-state space, while `h_t^j` means interaction history. | The draft now uses `H^j` for joint histories and `\mathcal S_h` / `\tilde h_t^j` for neural recurrent hidden states. |
| Done | MAWM equation used nested `unflatten(Dec(f(concat(...))))`. | The draft now uses numbered encode/update/decode equations: `z_t^j`, `\tilde h_t^j`, and `\hat\omega_{t+1}^j`. |
| Done | Projection formula used `M_d \odot \omega^{d,j}` where dimensions were ambiguous. | The draft now uses `P_d`, `P_u`, `\iota_d`, and `\iota_u` to make selection/insertion dimensions explicit. |
| Done | Residual predictor domain was not fully formalized. | The draft now defines `\mathcal T_\theta^{u,j}: H^j\times\Omega^{u,j}\times A^j\to\Omega^{u,j}`. |
| Done | Feature notation `f^i_{1,t}` was readable but not ideal. | The draft now uses `f^i_{t,k}` consistently in the observation definition. |
| Done | `\oplus` and bracket notation were mixed for residual assembly. | The draft now uses insertion operators for full-space assembly. |
| Done | RVR was empirical but not expressed as a Bernoulli sample mean. | The draft now states that `v_{i,k,t}` is a Bernoulli indicator and RVR is its empirical mean under the rollout distribution. |
| Done | Core equations were mostly unnumbered. | The main formal equations now have equation labels. |
| Remaining check | Method figure consistency should be visually rechecked. | The text references left/center/right panels; the visual figure should still be checked manually against the new `P_d/\iota_d` formalism. |

## I. Recommended Formal Notation Scheme

For the NeurIPS version, the cleanest scheme is:

| Concept | Recommended notation |
|---|---|
| Agents | `i \in \{1,\ldots,n\}` |
| Time | `t \in \{0,\ldots,T\}` |
| Feature index | `k \in \{1,\ldots,n_f\}` |
| Local observation | `\omega_t^i=(f_{t,1}^i,\ldots,f_{t,n_f}^i)` |
| Joint observation | `\omega_t^j=(\omega_t^1,\ldots,\omega_t^n)` |
| Local action | `a_t^i \in A_i` |
| Joint action | `a_t^j=(a_t^1,\ldots,a_t^n)` |
| Joint history | `h_t^j=\langle(\omega_\tau^j,a_\tau^j)\rangle_{\tau=0}^t` |
| Recurrent hidden state | `\tilde h_t^j` or `s_t^j`; avoid using `h_t^j` for this |
| Covered feature set | `\mathcal F^d` |
| Residual feature set | `\mathcal F^u` |
| Coverage mask | `M_d\in\{0,1\}^{n\times n_f}` or full vector mask after flattening |
| Full neural predictor | `\mathcal T_\theta^j` |
| Residual neural predictor | `\mathcal T_\theta^{u,j}` |
| Symbolic transition operator | `\mathcal T_s^j` |
| Raw neural prediction | `\hat\omega_{t+1}^{pre,j}` |
| Projected prediction | `\hat\omega_{t+1}^{proj,j}` |
| Residual-mode prediction | `\hat\omega_{t+1}^{res,j}` |
| Final rollout prediction | `\hat\omega_{t+1}^{post,j}` |
| Learned coherence | `RVR_pre` |
| Final covered-feature validity | `RVR_post` |
