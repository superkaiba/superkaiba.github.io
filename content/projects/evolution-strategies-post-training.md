---
title: What changes when post-training uses evolution strategies instead of RL?
status: Not started
order: 54.8
math: true
---

# What changes when post-training uses evolution strategies instead of RL?

**TL;DR:** Evolution strategies (ES), a zeroth-order method that perturbs the weights and keeps the perturbations that score well, now work for full-parameter LLM fine-tuning. Compare models post-trained with ES and with RL on the same rewards. Check how their weight updates, internal features, generalization, reward hacking and chain of thought differ.

[Qiu et al.](https://arxiv.org/abs/2509.24372) fine-tune all parameters of billion-parameter LLMs with ES and report that it beats RL baselines on several axes: tolerance to long-horizon rewards, robustness across base models, stability across runs, and less reward hacking. With a population of about 30 perturbed models per step, ES worked on Countdown and on a conciseness task where GRPO sometimes collapsed to nonsense short answers when the KL penalty was low. Earlier, [MeZO](https://arxiv.org/abs/2305.17333) showed that zeroth-order fine-tuning with only forward passes can work for large models. These papers focus on task performance. As far as I can tell, nobody has compared what ES and RL do inside the model, or what they do to alignment-relevant behavior.

**How the two methods explore.** RL with a policy gradient explores in *output* space. It samples outputs $y \sim \pi_\theta(\cdot \mid x)$ and updates by

$$
\nabla_\theta J(\theta) = \mathbb{E}_{y \sim \pi_\theta}\big[R(y)\, \nabla_\theta \log \pi_\theta(y \mid x)\big],
$$

so each token gets credit for the reward of its whole output. ES explores in *parameter* space. It samples noise $\epsilon \sim \mathcal{N}(0, I)$ and evaluates the perturbed model $\theta + \sigma\epsilon$:

$$
\nabla_\theta J_\sigma(\theta) = \frac{1}{\sigma}\,\mathbb{E}_{\epsilon}\big[R(\theta + \sigma\epsilon)\,\epsilon\big],
\qquad J_\sigma(\theta) = \mathbb{E}_\epsilon\big[R(\theta + \sigma\epsilon)\big].
$$

Two consequences follow. First, ES optimizes the reward averaged over a Gaussian ball of weights, so it prefers regions where the reward is high for many nearby weights (flat regions). Second, one perturbation acts on the whole episode, and there is no per-token credit. In particular, ES puts no direct pressure on individual chain-of-thought tokens. It can only select whole models whose reasoning tends to lead to reward.

**Initial directions:**

- **Matched comparison.** Post-train the same base model with ES, GRPO and SFT on the same tasks, matched at equal reward or equal KL divergence from the base. Most comparisons below are only fair at matched reward.
- **Weight updates.** RL updates are [sparse and avoid the principal directions of the weights](https://arxiv.org/abs/2511.08567). Check whether ES updates have the same structure, given that its raw noise is dense and isotropic.
- **Internal features.** Use model diffing (crosscoders or activation differences) to compare which features each method adds or changes.
- **Reward hacking.** Use environments with a known hack. Check whether ES hacks less at matched reward, or only because it moves less far from the base model.
- **Side effects of narrow training.** Train on narrow data known to cause emergent misalignment and compare how much each method generalizes it.
- **Chain of thought.** Add a CoT monitor to the reward and check whether ES also learns obfuscated reasoning, given that it has no per-token credit on the CoT.
- **Composition.** Repeat the $f(g(x))$ experiment from the [RL composition project](#rl-compositional-learning) with ES. Check whether ES also learns to compose skills, and through the same mechanism.

**Related projects:** [how RL teaches a model to compose skills it already has](#rl-compositional-learning), [is the chain of thought caught between the talker and the doer](#cot-between-talker-doer), [does Dynamic Fine-Tuning reduce emergent misalignment](#dft-emergent-misalignment), and [how few parameters RLVR needs when reusing a pretrained module](#minimal-rlvr-module).
