---
title: Do LLMs do distributional RL?
status: Not started
order: 13.8
math: true
---

# Do LLMs do distributional RL?

**TL;DR:** In mice, different dopamine neurons learn different "optimism levels" about future reward, so the population encodes a whole distribution of outcomes and not just the mean. Test whether LLMs solving reinforcement learning (RL) problems in context, and LLMs trained with RL, carry the same kind of distributional code in their activations.

Standard temporal difference (TD) learning tracks one number per state: the mean of future reward. [Distributional RL](https://arxiv.org/abs/1707.06887) instead learns the full distribution of returns, and it often helps deep RL agents. [Dabney et al. (2020)](https://www.nature.com/articles/s41586-019-1924-6) found evidence for this in the mouse ventral tegmental area. Different dopamine neurons had different reversal points (the reward size at which their response flips from negative to positive). Each neuron's reversal point matched how much more it responded to positive prediction errors than to negative ones. As a result, one reward could cause a positive error in pessimistic neurons and a negative error in optimistic neurons at the same time, and the reward distribution could be decoded from the population.

There is now good evidence that LLMs represent value and TD errors. [Demircan et al.](https://arxiv.org/abs/2410.01280) found sparse autoencoder (SAE) features in Llama 3 70B that track TD errors and Q-values during in-context RL, and showed that these features are causally involved. [Xu et al.](https://arxiv.org/abs/2602.00986) found sparse "value neurons" and "dopamine neurons" in models doing reasoning with verifiable rewards. Other work found a [linear value axis in Qwen3-8B](https://arxiv.org/abs/2606.17056) and showed that [LLMs are biased in-context RL learners](https://arxiv.org/abs/2405.11422). All of this work treats value as a single number. As far as I can tell, nobody has checked whether the value code in an LLM is distributional. (Distributional critics have been used to *train* LLMs, for example [quantile reward models](https://arxiv.org/abs/2409.10164) and [DistRLVR](https://iclr.cc/virtual/2026/10013479), but that is a different question.)

**Why asymmetric learning gives a distribution.** Let channel $i$ hold a value estimate $V_i$. It computes its own TD error and updates with a different learning rate for positive and negative errors:

$$
\delta_i = r + \gamma V_i(s') - V_i(s), \qquad
V_i(s) \leftarrow V_i(s) + \begin{cases} \alpha_i^+ \,\delta_i & \delta_i > 0 \\ \alpha_i^- \,\delta_i & \delta_i \le 0 \end{cases}
$$

Take the one-step case and write $R$ for the random target. At the fixed point, the expected update is zero:

$$
\alpha_i^+ \,\mathbb{E}\big[(R - V_i)_+\big] = \alpha_i^- \,\mathbb{E}\big[(V_i - R)_+\big].
$$

The $\tau$-expectile $e_\tau$ of $R$ minimizes $\mathbb{E}\big[\,|\tau - \mathbf{1}\{R < v\}|\,(R - v)^2\big]$ over $v$. Setting the derivative to zero gives

$$
\tau\,\mathbb{E}\big[(R - e_\tau)_+\big] = (1 - \tau)\,\mathbb{E}\big[(e_\tau - R)_+\big].
$$

These two conditions are the same when

$$
\tau_i = \frac{\alpha_i^+}{\alpha_i^+ + \alpha_i^-}.
$$

So a channel with $\alpha^+ > \alpha^-$ converges to an upper expectile (optimistic), and a channel with $\alpha^+ < \alpha^-$ converges to a lower one (pessimistic). A set of channels with different $\tau_i$ encodes a set of expectiles, and a set of expectiles determines the distribution. This gives the main signature to look for: each channel's reversal point $e_{\tau_i}$ should increase with its asymmetry $\tau_i$.

**A confound to rule out.** An in-context learner can see all past rewards in its context, and next-token prediction already gives a distribution over the next reward token. So "the distribution can be decoded somewhere" is not enough. The interesting claim is narrower: a compressed summary at the option token, updated step by step, made of channels with different asymmetries. The tests below target that claim. A second confound is a mean code plus a separate variance code. That also encodes spread, but it predicts one reversal point for all channels.

**Initial directions:**

- **Build tasks where the mean is not enough.** Use in-context bandits and two-step tasks in the style of Demircan et al., with numeric rewards in the text. Pair options with equal means and different shapes (bimodal against unimodal, left skew against right skew). The two-step task checks the distribution over returns, not just over the immediate reward.
- **Check behavior first.** At equal mean, does the model's choice depend on the variance or skew of the reward? Can it state quantiles of an option's reward when asked? If behavior ignores shape, a distributional code is less likely to be present or used.
- **Find value and TD-error features.** Use SAEs or the neuron-level method of Xu et al. to find units that respond to reward prediction errors. For each unit, fit separate slopes for positive and negative errors and estimate its reversal point.
- **Test the Dabney signature.** Check whether reversal points differ across units more than noise allows, whether asymmetry predicts reversal point, and whether one reward gives errors of opposite sign in different units. Then try to decode the reward distribution from the population at the option token, and compare with a model that only stores mean and variance.
- **Intervene.** Steer along the optimistic or pessimistic units, or ablate one group. A distributional code that the model uses should shift choices toward risk seeking or risk aversion while leaving the mean estimate mostly unchanged.
- **Compare training regimes.** Run the same analysis on a base model, its instruct version, and an RL-trained reasoning model. Binary verifiable rewards make the return distribution a Bernoulli, so every expectile is a function of the mean alone. RL with graded or multimodal rewards may be needed before a richer code appears, which would itself be an interesting result.

A positive result would show that LLMs, like the brain, may have picked up distributional value coding without being trained for it. It would also give a handle on risk attitudes: if optimistic and pessimistic channels can be found and steered, that is a direct way to make an agent more cautious. A negative result would still be useful. It would suggest that the TD-like features found so far are mean-only, and that risk-sensitive behavior in LLMs comes from somewhere else.

**Related projects:** [whether different layers perform different stages of belief updating](#layerwise-belief-updating), [whether the model simulates a grader persona](#grader-representation), and [a scaling law for transfer between RL environments](#rl-transfer-scaling-law).
