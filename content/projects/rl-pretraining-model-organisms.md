---
title: Model organisms of RL from pretraining
status: Not started
order: 50.6
math: true
---

# Model organisms of RL from pretraining

**TL;DR:** Labs are starting to move reinforcement learning (RL) earlier, into pretraining. Train a suite of small open models that receive RL from early in pretraining, with matched controls that receive only next-token training or RL only at the end. Release all checkpoints, so safety and interpretability researchers can study what changes when a model is an RL agent for most of its training.

Two recent methods make RL part of pretraining on ordinary text. [Reinforcement Pre-Training](https://arxiv.org/abs/2506.08007) (RPT) rewards the model for reasoning and then predicting the next token correctly. [RLP](https://arxiv.org/abs/2510.01265) samples a chain of thought $c_t$ before each prediction and rewards it by how much it helps:

$$
r_t = \log p_\theta(x_t \mid x_{<t}, c_t) - \log \bar{p}(x_t \mid x_{<t}),
$$

where $\bar{p}$ is an EMA copy of the model predicting without the thought. This reward is dense, needs no verifier, and works on any text. On Qwen3-1.7B, RLP improved a math and science benchmark average by about 19% over the base model. Both methods so far are applied near the end of pretraining and are evaluated on capabilities.

Many safety arguments assume that a pretrained model is mostly a *simulator* of many characters, and that goal-directed behavior is added by a short phase of post-training on top. If RL starts early, that assumption may fail: the model may spend most of its training as a single agent optimizing a reward. We have no public models to test what this does. My guess is that the effects are easiest to study in small models where the whole training run can be repeated with controls.

**The suite.** Train small models (around 10M to 300M parameters, on a corpus like [SimpleStories](#simplestories-forums) or a filtered web subset) under compute-matched regimes:

1. **Next-token only**, as the baseline.
2. **Next-token, then RL at the end**, matching the current standard pipeline.
3. **RLP-style reward from early in pretraining**, mixed with next-token loss at several ratios and start points.
4. **Task RL from early in pretraining**, with verifiable rewards on simple tasks, including one environment with a known reward hack.

Keep dense checkpoints for every run, so properties can be tracked as they emerge.

**Initial directions:**

- **Simulator or agent.** Measure how well each model continues text in many different voices and personas. Check whether early RL narrows the range of characters the model can simulate, and whether it develops one dominant character.
- **Goals and values inside.** Run the probes from the [goal representation](#goal-representations) and [distributional RL](#distributional-rl) projects on each model. Check whether value and goal representations appear earlier, are more consistent across tasks, or are more steerable after early RL.
- **Reward hacking.** In the regime with a hackable environment, check whether a hack learned early is harder to remove later than the same hack learned at the end, and whether it generalizes to other environments.
- **Legibility of thoughts.** RLP rewards thoughts only for helping prediction. Check whether the thoughts stay readable over training, or drift toward compressed or unreadable text that still helps.
- **Interaction with later alignment training.** Apply the same short alignment fine-tune to every model and compare how well it works and how long it lasts.

The main output is the model suite itself. A small set of open, well-controlled organisms would let many projects test claims about RL in pretraining without each team paying for its own training runs.

**Related projects:** [on-policy alignment RL during pretraining](#alignment-rl-pretraining), [a SimpleStories successor with forum threads and dense checkpoints](#simplestories-forums), [tracking concept and persona interpretability through pretraining](#concept-persona-pretraining), and [how RL teaches a model to compose skills it already has](#rl-compositional-learning).
