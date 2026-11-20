# Can pessimistic risk estimates reduce reward hacking without teaching models to hide it?

**TL;DR:** Safety penalties in LLM training usually act on the average harm or the average grader score, and averages hide rare disasters. Charge an upper expectile of the danger estimate instead, which leans toward the worst plausible case, and test where this helps against reward hacking: in a controller that filters actions without training the policy, and as a training penalty, where the main risk is that the model learns to hide its hacks.

Most constrained approaches keep the average harm below a limit. [Safe RLHF](https://arxiv.org/abs/2310.12773) trains separate reward and cost models and constrains the expected cost. Two models with the same average harm can still be very different: one is slightly harmful every time, while the other is perfectly safe 99 times out of 100 and very harmful once. Work on tail risk handles this with CVaR, both in robotics ([WCSAC](https://doi.org/10.1609/aaai.v35i12.17272)) and for LLMs ([risk-averse fine-tuning](https://arxiv.org/abs/2501.06911)). On the reward side, [reward model ensembles with conservative objectives](https://arxiv.org/abs/2310.02743) reduce overoptimization, which suggests that disagreement between graders carries useful information about hacks.

**Why expectiles.** The $\tau$-expectile $e_\tau$ of a danger estimate $D$ solves

$$
\tau\,\mathbb{E}\big[(D - e_\tau)_+\big] = (1 - \tau)\,\mathbb{E}\big[(e_\tau - D)_+\big].
$$

At $\tau = 0.5$ it is the mean, and as $\tau \to 1$ it approaches the maximum. For $\tau \ge 1/2$ it is a coherent risk measure, and expectiles are [the only coherent risk measures that are also elicitable](https://arxiv.org/abs/1303.1690). Elicitable means a model can be trained to output it directly with an asymmetric squared loss, and its outputs can be checked against the violations that actually happen. It is also what a channel with asymmetric learning rates converges to (see [Do LLMs do distributional RL?](#distributional-rl)), so the same math shows up in dopamine neurons and in this safety setting.

A small example: suppose four sampled hypotheses about what an instruction means give an action's added probability of a violation as 0.01, 0.01, 0.01 and 0.20. The mean is 0.0575 and the 0.9-expectile is 0.1525. With 0.1 left in the risk budget, the mean lets the action through and the expectile blocks it. The action looks safe under three readings of the rule, and one plausible reading makes it risky.

**The main risk: teaching the model to hide.** Penalizing hacks that a detector catches can teach the model to evade the detector. With enough optimization against a chain-of-thought monitor, agents [learn obfuscated reward hacking](https://arxiv.org/abs/2503.11926). Pessimism may make this worse. Take a cheat that pays $+1$ if not caught and $-1$ if caught, with catch probability $q$. Its lower $\tau$-expectile is

$$
e = \frac{\tau(1-q) - (1-\tau)q}{\tau(1-q) + (1-\tau)q}.
$$

At $\tau = 0.1$, going from $q = 0.10$ to $q = 0.01$ raises the cheat's value from 0 to 0.83, while its mean only goes from 0.80 to 0.98. So a pessimistic objective rewards better concealment much more strongly than the mean does. A frozen danger head that reads the policy's own activations has a related problem: RL can teach models to [evade latent-space monitors](https://arxiv.org/abs/2506.14261) without any gradient through the monitor. Whether training against a detector produces honesty or evasion seems to depend on [the detector's accuracy and the KL penalty](https://arxiv.org/abs/2505.13787).

My guess is that the penalty works best when it depends on predicted violations of intent, since hiding a hack from a detector then gains nothing. This is close to using a predictor as a guardrail, as in the [Scientist AI proposal](https://arxiv.org/abs/2502.15657) and the [Bayesian oracle bounds](https://arxiv.org/abs/2408.05284), where an upper expectile would sit between the posterior mean and the most cautious plausible hypothesis.

**Initial directions:**

- **Expectile charging in a controller.** Use a predictor to estimate how much each candidate action raises the probability of violating the instructions, under several sampled hypotheses about what they mean. Compare a controller that charges the mean against one that charges an upper expectile, on coding environments with known exploits. Measure the exploit rate and success on clean tasks across $\tau$.
- **Pessimistic training penalties.** Train against an ensemble of graders with a lower expectile of reward and an upper expectile of cost. Compare four arms: the average objective, the pessimistic objective throughout, the pessimistic objective early followed by the average, and the average objective with [inoculation prompting](https://arxiv.org/abs/2511.18397). The third arm tests whether an early penalty on hacking keeps working after it is removed.
- **Measure hiding directly.** Use one hack detector for the penalty and a held-out one for evaluation. A growing gap between them means the model is learning to hide hacks.
- **Frozen danger heads.** Compare a separate frozen danger model that only reads text with a frozen head on the policy's own trunk. Track the frozen head, a held-out head and an independent judge over training. Periodically fit a fresh probe on current activations to tell new hacking behavior apart from representations that drifted away from the frozen head.
- **Look inside.** Check whether pessimistic training leaves a pessimistic value channel in the model, whether it survives after switching back to the average objective, and whether the gap between optimistic and pessimistic channels predicts when the model is about to attempt a hack.

A positive result would give a single parameter ($\tau$) for how cautious an agent should be, with an estimate that can be trained and audited. A negative result, especially the model learning to hide hacks faster under pessimism, would be a useful warning against tail penalties in RL training and would point toward using them only at inference time.

**Related projects:** [whether LLMs do distributional RL](#distributional-rl), [viewing models as reward addicts](#reward-addicts), [evolutionary algorithms as a safer alternative to RL](#evolution-strategies-post-training), [when model behavior is internally detectable](#internal-detectability), and [whether the model simulates a grader persona](#grader-representation).
