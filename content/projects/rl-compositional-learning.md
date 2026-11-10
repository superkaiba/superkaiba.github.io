---
title: How does RL teach a model to compose skills it already has?
status: Not started
order: 54.75
math: true
---

# How does RL teach a model to compose skills it already has?

**TL;DR:** RL with outcome rewards can teach an LLM to compute $f(g(x))$ when it already knows $f$ and $g$, and this skill transfers to new tasks. Find the mechanism. Check whether the model reuses its existing circuits for $f$ and $g$, what RL adds to connect them, and why rejection fine-tuning on the same data does not produce the same skill.

[Yuan et al.](https://arxiv.org/abs/2509.25123) give a clean testbed. Atomic skills are string transformation functions with renamed identifiers, so the model cannot have memorized them. A model is first trained to predict the output of each atomic function. RL on two-function compositions then lifts accuracy on unseen three-function compositions from near zero to about 30%, and on four-function compositions to about 15%. Rejection fine-tuning (RFT) on the same two-function problems does not give this generalization, and RL on atomic problems alone does not either. The compositional skill also transfers to a different task (Countdown), as long as the model already has that task's atomic skills. Behaviorally, RL removes errors where the model ignores the composition, and the remaining errors are mostly errors on the atomic steps.

This sits inside a broader debate on whether RL teaches new skills or only reweights existing ones. RL updates are [sparse](https://arxiv.org/abs/2511.08567) and avoid the principal directions of the weights, and [GRPO changes less than SFT](https://arxiv.org/abs/2507.10616), mostly amplifying what the base model can already do. Composition is a good case to study because the new skill is precisely defined and is built from parts that can be located before RL starts. As far as I can tell, nobody has looked at what changes inside the model when RL teaches composition.

**Hypotheses for the mechanism.** There are a few distinct ways the model could implement $f(g(x))$:

1. **Explicit chaining.** The model writes $z = g(x)$ in its chain of thought and then applies $f$ to the written $z$. RL mainly teaches the habit of writing the intermediate.
2. **Latent chaining.** The model computes $z$ internally and feeds it into the circuit for $f$ within one forward pass, using the same circuits as for the atomic tasks.
3. **New composite circuits.** RL builds new circuits for specific pairs $(f, g)$ that do not reuse the atomic ones.

Only 1 and 2 would explain transfer to Countdown and to deeper compositions. The test that separates 2 from 3 is **intermediate patching**. Take two inputs $x$ and $x'$ and let $z' = g(x')$. Patch the model's internal representation of the intermediate on input $x$ with the one from $x'$. If composition reuses the atomic $f$ circuit, the output should become $f(z')$:

$$
\mathrm{Pr}\big[\text{output} = f(z') \mid \text{patch } z \leftarrow z'\big] \approx 1.
$$

The same patch can be run before and after RL. The interesting case is if the intermediate is already represented before RL but the model fails to use it.

**Initial directions:**

- **Reproduce the testbed** on a model small enough to analyze, and keep checkpoints across the RL run.
- **Locate the atomic circuits before RL.** For each atomic function, find the heads, MLP features or SAE latents that carry it, using attribution graphs or patching on the atomic tasks.
- **Measure reuse after RL.** On composite tasks, check whether the same components are active and causally necessary. Compute the overlap between the atomic and composite circuits.
- **Find what RL added.** Compare the weights and activations before and after RL. Check whether the change is concentrated in a few "glue" components that route the output of $g$ into $f$, and whether the same components change in RL runs on other tasks.
- **Compare RL with RFT.** Run the same analysis on the RFT model trained on the same problems. Check whether RFT also builds the glue but fails to generalize, or never builds it.
- **Explain the transfer.** Take the weight difference from RL on the string task and add it to a model that only knows the Countdown atomics. If composition transfers, the glue is task-general, and the patching test should work on Countdown as well.
- **Track emergence over training.** Check when in the RL run the intermediate becomes decodable, when patching starts to work, and whether these come before the jump in composite accuracy.

A clear mechanism would give a concrete answer to the "new skills or reweighting" debate for one case. It would also connect to [my work on a complexity-based theory of compositionality](https://arxiv.org/abs/2410.14817): my guess is that composition through reused parts gives representations with lower complexity than composition through new composite circuits.

**Related projects:** [a scaling law for transfer between RL environments](#rl-transfer-scaling-law), [how few parameters RLVR needs when reusing a pretrained module](#minimal-rlvr-module), and [whether LLM neurons grow by recursive generalization during training](#recursive-generalization-training).
