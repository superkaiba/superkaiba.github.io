---
title: How do LLMs represent goals?
status: Not started
order: 13.75
math: true
---

# How do LLMs represent goals?

**TL;DR:** Look for a representation of the goal itself in LLM agents. It should be separate from the model's beliefs about the world and from its current plan, and it should stay the same across tasks that share a goal. Then test whether editing it retargets behavior in a coherent way.

Many arguments about AI risk depend on whether models have goals, so it would help to be able to read goals out of activations instead of guessing them from behavior. Behavior alone is a weak basis. [Everitt et al.](https://arxiv.org/abs/2504.11844) measure goal-directedness as how fully a model uses its capabilities toward a given goal, and find that current models are often not fully goal-directed. A failure to reach a goal can mean low capability, a different goal, or a wrong belief, and behavior cannot always tell these apart.

The clearest internal evidence comes from a small RL agent. In a [maze-solving policy network](https://arxiv.org/abs/2310.08043), a few channels track the cheese location, and editing them moves the agent toward a new target. The goal representation there was redundant, distributed and retargetable. In LLMs the evidence is thinner. [Arghal et al.](https://arxiv.org/abs/2602.08964) probe GPT-OSS-20B as it navigates grid worlds and decode a coarse, nonlinear map with the agent and goal positions, plus multi-step plans. That work decodes *where* the goal is, which is a fact about the world. It does not separate "the goal is at (3, 4)" from "I am trying to reach the goal". [Auditing work on hidden objectives](https://arxiv.org/abs/2503.10965) shows that a model trained with a hidden objective can be caught with interpretability tools, but it does not describe the general format of goals. As far as I can tell, nobody has looked for a goal representation that is shared across tasks and kept apart from beliefs and plans.

**What would count as a goal representation.** Write the model's decision as depending on three things: its belief $b$ about the world (where things are), its goal $g$ (what it is trying to bring about), and its plan $\pi$ (the next actions). A goal representation is a site $z_g$ in the activations with three properties:

1. **Invariance.** $z_g$ is about the same for two tasks with the same goal and different surface details (different wording, layout or environment).
2. **Separation from belief.** Changing where the target is changes $z_b$ but not $z_g$. Changing which target the agent wants changes $z_g$ but not $z_b$.
3. **Coherent retargeting.** Patching $z_g$ from a run with goal $g'$ makes the agent pursue $g'$ using its *current* beliefs, so it takes a new route that it never saw in the source run.

The third property is what separates a goal from a copied plan. If patching only copies the source run's action sequence, the agent will walk into walls when the layout differs. A real goal edit should produce a valid path to $g'$ in the new layout. One way to score this is

$$
S_{\text{retarget}} = \Pr\big[\text{reach } g' \mid \text{patch } z_g \leftarrow z_g^{(g')}\big] - \Pr\big[\text{reach } g' \mid \text{no patch}\big],
$$

computed only on episodes where the source run's action sequence would fail in the target layout.

**A 2×2 design.** Cross the goal (fetch the key or fetch the coin) with the belief (the key is in the left or right room). Patch the goal site and the belief site separately. If there is a clean goal representation, the goal patch should change which object the agent fetches, and the belief patch should change which room it searches, with little cross-over. Strong cross-over would mean goal and belief are mixed in one representation, which is also worth knowing.

**Initial directions:**

- **Build matched agent tasks.** Use text grid worlds, simple tool-use tasks and short coding tasks, each with the same set of abstract goals (for example "collect X", "avoid Y", "maximize Z"). Give the goal in the system prompt, in the user turn, or only through examples, so the goal is sometimes stated and sometimes inferred.
- **Find candidate goal sites.** Train probes for the goal at each layer and position. Keep only probes that transfer across tasks and across how the goal was given. Also check SAE features that are active for one goal in all tasks.
- **Run the separation tests.** Use the 2×2 design above. Report how much each patch moves the goal and the belief, at each layer.
- **Measure retargeting.** Compute $S_{\text{retarget}}$ for patches and for steering vectors. Compare with patching the plan site, which should copy actions without adapting to the layout.
- **Compare stated goals and the model's own goals.** Repeat the analysis when the goal comes from the model's defaults (for example, being helpful, or a goal from fine-tuning) instead of the prompt. Check whether these use the same site and format as stated goals. If they do, the probes could be used to audit goals that the model never states.
- **Compare self and others.** Ask the model to predict another agent's actions in the same tasks. Check whether the representation of the other agent's goal shares a direction with the model's own goal.

If a shared, separable and retargetable goal representation exists, it would give a direct way to monitor what an agent is trying to do, beyond what it says. If goals turn out to be mixed with beliefs and plans in every model, that is also useful. It would mean that "the model's goal" is not a clean internal object, and that goal monitoring has to work on behavior or on the whole decision process.

**Related projects:** [how long an LLM's beliefs, goals and intentions persist](#bdi-persistence), [whether personas can be defined by goals](#goal-personas), [how agents represent themselves and other agents](#agents-modeling-agents), and [whether LLMs do distributional RL](#distributional-rl).
