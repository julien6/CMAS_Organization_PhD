# Simulated NeurIPS Reviewer Reports for NS-MAWM

These reports are intended as an internal stress test of the current manuscript. They assume the paper contains the strengthened abstract, horizon-wise rollout analysis, explicit rule examples, RVR diagnostics, and the lightweight MPC/CEM planning experiment.

## Reviewer 1: Methodological Reviewer

**Overall score:** 7: Accept  
**Confidence:** 3: Moderate

### Summary

This paper proposes NS-MAWM, a neuro-symbolic extension of multi-agent world models that uses partial symbolic transition knowledge to improve long-horizon semantic reliability under partial observability. The method decomposes covered and uncovered state components, and studies three integration mechanisms: soft regularization, hard projection, and residual symbolic dynamics. The paper evaluates prediction accuracy, rule violations, correction magnitude, robustness to partial/noisy rules, and a lightweight model-based planning setting.

### Strengths

- The central problem is well motivated: long-horizon drift in multi-agent world models is a real obstacle for planning and imagined rollouts.
- The covered/residual decomposition gives the paper a clear conceptual contribution rather than a collection of heuristics.
- The method variants are now clearly differentiated: regularization provides a soft bias, projection enforces covered-state validity, and the residual model changes the prediction target.
- The evaluation links semantic consistency to downstream utility through planning, which makes the work more compelling than a purely diagnostic consistency paper.
- The horizon-wise analysis and RVR correction diagnostics are useful and directly support the claims.

### Weaknesses

- The theoretical analysis remains lightweight. The paper gives conditional arguments about projection and residual decomposition but does not prove strong guarantees for learned rollouts.
- The method depends on symbolic rules that are externally provided. The paper discusses this limitation, but the cost of rule engineering could be clearer.
- The comparison to modern latent world models is present but still somewhat shallow. A stronger Dreamer/RSSM implementation would make the empirical story more decisive.

### Questions

- How sensitive are the planning gains to the quality of the symbolic abstraction?
- Are the symbolic masks manually defined per environment, or can they be derived from environment metadata?
- Would the residual formulation remain stable when symbolic coverage is sparse but the symbolic features are highly coupled with uncovered features?

### Recommendation

I lean accept. The paper makes a clear and useful contribution for neuro-symbolic world models in MARL, and the revised experiments now demonstrate both semantic and decision-level value. The main limitation is that the empirical comparison could be broader, but the proposed framework is sufficiently novel and well supported.

## Reviewer 2: Empirical World-Model Reviewer

**Overall score:** 5: Borderline Reject  
**Confidence:** 4: High

### Summary

The paper introduces a neuro-symbolic multi-agent world model that incorporates partial symbolic transition rules through regularization, projection, or residual prediction. The empirical section studies rollout error, rule violation rates, correction magnitudes, robustness to rule dropout/noise, and a planning experiment.

### Strengths

- The paper now addresses the important question of whether semantic consistency translates into better planning.
- Horizon-wise rollout plots are valuable and show that semantic constraints matter most when compounding errors appear.
- The ablations isolate several possible explanations: symbolic features, post-hoc correction, regularization, projection, and residual prediction.
- Results are reported with multiple seeds and uncertainty, which improves credibility.

### Weaknesses

- The main baselines are still not fully satisfying for a NeurIPS empirical paper. The RSSM/Dreamer-style comparison is useful, but the implementation details and tuning budget should be described more explicitly.
- The planning experiment is lightweight. It shows that model consistency helps MPC/CEM-style planning, but it does not show end-to-end policy learning or large-scale control.
- Some environments remain relatively structured. SMACv2 helps, but the strongest results appear to come from settings where the symbolic rules are naturally aligned with the task.
- The symbolic rules are hand-designed, which may limit applicability.

### Questions

- Were all baselines tuned with the same compute budget?
- Does the RSSM/Dreamer-style baseline use the same observations and action conditioning as NS-MAWM?
- How often does hard projection hurt return when rules are noisy or incomplete?

### Recommendation

I am borderline negative. The paper is much stronger than a pure consistency study, but I am not fully convinced the empirical evaluation is broad enough for NeurIPS. I would be more positive with either a stronger large-scale baseline comparison or a more substantial downstream control experiment.

## Reviewer 3: Balanced MARL / Neuro-Symbolic Reviewer

**Overall score:** 6: Weak Accept  
**Confidence:** 3: Moderate

### Summary

The paper studies how partial symbolic knowledge can be incorporated into multi-agent world models to reduce semantic drift under partial observability. It proposes NS-MAWM, which separates covered and uncovered dynamics and evaluates soft, hard, and residual integration modes. The empirical results suggest improvements in long-horizon prediction, rule validity, robustness under partial rule coverage, and planning utility.

### Strengths

- The paper identifies a meaningful gap between neural multi-agent world models and symbolic consistency constraints.
- The problem formulation is now coherent and tied to the evaluation.
- The claim-to-evidence structure is unusually clear: formal construction, conditional deductive support, and empirical claims are separated.
- The RVR pre/post distinction and correction magnitude analysis address an important metric validity concern.
- The lightweight planning experiment is enough to show that semantic reliability can matter for decision-making.

### Weaknesses

- The paper is dense and may exceed the patience of some reviewers. Some tables could move to appendix after final page compression.
- The qualitative rollout analysis would be stronger as an actual visual figure rather than only a table.
- The scalability discussion is plausible but not fully demonstrated experimentally.
- Rule design remains manual, and the paper does not solve symbolic knowledge acquisition.

### Questions

- Which variant should practitioners use by default: projection or residual dynamics?
- Can the method handle contradictory symbolic rules, or are inconsistencies assumed to be filtered before training?
- Does semantic consistency ever trade off against predictive accuracy on uncovered variables?

### Recommendation

I lean weak accept. The paper has a clear contribution, strong motivation, and enough empirical support to be useful to the community. The strongest remaining concern is empirical breadth, but the planning and robustness analyses substantially reduce the risk.

## Exact NeurIPS-Style Figures to Prioritize

1. **Main method diagram.**  
   Show neural predictor, symbolic transition operator, coverage mask, projection/residual path, and final rollout. This should be the first figure and should make the method understandable in under one minute.

2. **Horizon-wise rollout degradation plot.**  
   Plot prediction error and/or semantic violation rate as a function of rollout horizon. This is the central world-model figure because it shows compounding error.

3. **Planning utility figure.**  
   Plot planning return or success rate against invalid imagined plan rate. This makes the bridge from semantic reliability to decision quality visually explicit.

4. **RVR and correction magnitude diagnostic.**  
   Use either histograms or grouped bars to show RVR_pre, RVR_post, and correction magnitude. The point is to show that low RVR_post is not merely a trivial consequence of projection.

5. **Qualitative rollout panel.**  
   Show side-by-side neural and NS-MAWM rollouts on the same initial state/action sequence. Highlight the first invalid transition in the neural model and the corresponding corrected or avoided transition in NS-MAWM.

6. **Robustness curve.**  
   Plot symbolic coverage or rule dropout on the x-axis and semantic validity / planning return on the y-axis. This directly answers whether the method survives partial or noisy symbolic knowledge.

## Simulated Meta-Review

**Meta-review recommendation:** Borderline Accept  
**Confidence:** Moderate

The reviewers agree that the paper has improved substantially and now presents a coherent contribution: using partial symbolic transition knowledge to improve semantic reliability in multi-agent world models under partial observability. There is consensus that the problem is relevant to NeurIPS, that the covered/residual formalism is a useful organizing principle, and that the paper is now much clearer about what is guaranteed formally versus what is supported empirically.

The main positive points are the strengthened claim-to-evidence alignment, the horizon-wise rollout analysis, the RVR pre/post distinction, the explicit rule examples, and the lightweight planning experiment. These additions make the work feel like a world-model paper with decision relevance rather than a purely diagnostic consistency study. The strongest reviewer finds the method principled and useful; the balanced reviewer views the empirical package as sufficient for weak acceptance.

The main remaining concern is empirical depth. One reviewer remains skeptical that the planning experiment is too lightweight and that the RSSM/Dreamer-style baseline is not strong enough to fully contextualize the contribution. There is also some concern that symbolic rules are manually specified and that the paper does not solve rule acquisition. These points are acknowledged in the limitations, but they remain the most likely source of a weak-reject review.

As area chair, I would weigh the paper as a credible borderline-accept submission. The contribution is not a broad new world-model architecture, but it cleanly identifies and studies an important failure mode: semantically invalid long-horizon multi-agent rollouts. The revised evaluation now shows that symbolic reliability affects both rollout validity and model-based planning under matched budgets. The work is therefore likely to be useful to researchers studying model-based MARL, neuro-symbolic learning, and constrained dynamics. I recommend acceptance if the final version keeps the claims conditional, reports all results with uncertainty over seeds, and clearly documents the symbolic rule inventory and baseline tuning protocol.

### Most likely final decision drivers

- **Accept driver:** reviewers buy the argument that long-horizon semantic reliability is an under-studied but important axis for multi-agent world models.
- **Reject driver:** reviewers decide the downstream planning experiment and modern WM baseline are still too lightweight.
- **Best rebuttal angle:** emphasize that NS-MAWM is orthogonal to RSSM/Dreamer-style latent architectures, that all comparisons use matched planner budgets and seeds, and that the paper deliberately separates formal construction claims from empirical utility claims.
- **Most useful final polish:** put the planning utility figure and horizon-wise rollout figure early enough that reviewers see the impact before getting lost in details.

## Rebuttal Strategy for Likely Reviewer Comments

### Comment A: "The method is just projection or post-hoc correction."

**Response strategy.**  
Emphasize that projection is only one instantiation of NS-MAWM. The contribution is the covered/residual framework and shared interface that supports three distinct mechanisms: soft learned consistency, hard covered-feature enforcement, and residual symbolic dynamics. Point to the post-correction baseline: if the method were only late repair, MAWM + post-correction would match NS-MAWM projection/residual, but the reported correction magnitudes, RVR$_{pre}$, and planning results separate these cases.

**Evidence to cite.**  
Use the baseline table, RVR correction table, RVR diagnostic figure, and planning utility figure.

### Comment B: "The comparison to Dreamer/RSSM is weak."

**Response strategy.**  
State clearly that NS-MAWM is orthogonal to latent WM architectures. The paper includes an RSSM/Dreamer-style reference point to contextualize the empirical results, but the contribution is not a new latent backbone. The framework can be attached to such models whenever symbolic predicates are decoded, supervised, or exposed at the transition boundary.

**Evidence to cite.**  
Use the related-work paragraph, the baseline table, and the reproducibility section describing matched budgets.

### Comment C: "The symbolic rules are hand-designed and environment-specific."

**Response strategy.**  
Agree with the limitation, then narrow the claim: the paper does not solve rule acquisition. It studies how partial symbolic transition knowledge should be represented, integrated, and evaluated once available. The rules are local transition constraints, not complete simulators, and the rule coverage table reports which features are covered and which remain residual.

**Evidence to cite.**  
Use the concrete rule examples, rule-coverage table, and limitations section.

### Comment D: "Semantic validity may not matter for reward."

**Response strategy.**  
Point to the shared MPC/CEM experiment and invalid-plan analysis. The decision claim is intentionally empirical and conditional: when symbolic coverage is informative, fewer invalid imagined plans can improve action selection under a matched planning budget. The paper does not claim that semantic validity always improves reward.

**Evidence to cite.**  
Use the planning protocol table, planning/OOD table, planning utility figure, and statistical interpretation paragraph.

### Comment E: "RVR is just another metric."

**Response strategy.**  
Frame RVR as a diagnostic that separates learned semantic coherence from enforced semantic validity. The important evidence is not zero RVR$_{post}$ alone, but the combination of RVR$_{pre}$, correction magnitude, trigger type, rollout error growth, invalid plan rate, and return.

**Evidence to cite.**  
Use the RVR correction table, trigger analysis, RVR diagnostic figure, and the reported association between invalid imagined plans and return.

### Comment F: "The method may fail when rules are wrong or sparse."

**Response strategy.**  
Agree and cite this as an explicitly tested or limited regime. The paper only claims covered-feature validity under correct masks and rules. Rule dropout/noisy-rule experiments measure graceful degradation, while the limitations state that hard symbolic modes can be harmful when rules are misspecified.

**Evidence to cite.**  
Use the rule-dropout table, robustness paragraph, and limitations section.
