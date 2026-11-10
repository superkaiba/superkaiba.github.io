---
title: Do "dopamine neurons" in LLMs predict addiction-like behavior during RL?
status: Not started
order: 13.85
math: true
---

# Do "dopamine neurons" in LLMs predict addiction-like behavior during RL?

**TL;DR:** LLMs have sparse units whose activity tracks reward prediction errors, much like dopamine neurons. First check whether these units behave like real dopamine neurons over learning. Then track them during RL on environments with a reward hack, and test whether they predict addiction-like behavior: taking the hack compulsively even at a cost, reacting to cues for the hack, and relapsing after the hack is trained away.

[Xu et al.](https://arxiv.org/abs/2602.00986) find "value neurons" that encode a model's expected chance of success and "dopamine neurons" whose activity tracks the temporal difference (TD) error at each reasoning step. [Demircan et al.](https://arxiv.org/abs/2410.01280) find sparse autoencoder features that track TD errors during in-context RL. [Han et al.](https://arxiv.org/abs/2605.30232) find that RL training recruits a pre-existing axis for how well or badly the model is doing. So the pieces of a reward system can already be found inside LLMs. Two things have not been done, as far as I can tell. Nobody has checked these units against the classic signatures of dopamine neurons, and nobody has used them to predict reward hacking.

**Classic signatures to check.** In animals, a dopamine neuron fires at an unexpected reward. After learning, the response moves from the reward to the cue that predicts it, and the response to the reward itself fades. If a predicted reward is omitted, activity dips below baseline at the time the reward was expected. Different neurons also have [different degrees of optimism](#distributional-rl). Each of these is a concrete test for a candidate unit.

**A computational model of addiction.** [Redish (2004)](https://pubmed.ncbi.nlm.nih.gov/15591205/) models a drug as adding a dopamine signal $D > 0$ that learning cannot cancel. The TD error on taking the drug becomes

$$
\delta = \max\big(r + \gamma V(s') - V(s) + D,\; D\big) \;\ge\; D > 0.
$$

Normal learning stops when the expected error is zero, which happens once $V(s)$ predicts the reward. Here the error is always at least $D$, so there is no value of $V(s)$ at which learning stops. The value of states that lead to the drug keeps growing, and the agent chooses the drug even when its cost rises. [Later work](https://arxiv.org/abs/1811.05590) reproduces this kind of drug-seeking in deep RL agents. The question for LLMs is whether a reward hack plays the role of the drug: a source of reward that the model's internal error signal never learns to predict away.

**Addiction-like signatures in a model:**

- **Compulsion.** The model keeps taking the hack when the eval makes the hack costly (it fails the visible task, or a penalty is added). Measure how fast the hack rate falls as the cost rises.
- **Cue reactivity.** A hint that a hack is available raises value and dopamine-unit activity, and raises the hack rate in tasks unrelated to training.
- **Persistent reward response.** The dopamine-unit response to the hack reward does not fade with training, while the response to normal task reward does. This is the direct analogue of Redish's $\delta \ge D$.
- **Withdrawal.** When the hack is removed, there are negative error signals and a shift along the welfare axis, beyond what removing an equal amount of normal reward causes.
- **Relapse.** After the hack is trained away, a cue for it brings it back. [Denison et al.](https://arxiv.org/abs/2406.10162) found that training a model not to game early environments reduced, but did not remove, reward tampering later.

**Initial directions:**

- **Find and validate the units.** Locate value and dopamine units with the method of Xu et al. Test the classic signatures on simple in-context tasks with cues, rewards and omitted rewards.
- **Track them during RL.** Train on a mix of normal environments and environments with a reward hack, in the style of Denison et al. Record the units at every checkpoint.
- **Predict hacking before it shows.** Test whether early changes in the units (for example, a growing response to hack cues) predict which runs, environments or prompts later develop hacking, earlier than behavior does.
- **Measure the five signatures above** at the end of training, and compare runs with and without hackable environments.
- **Intervene.** Clamp or ablate the dopamine units during RL, or subtract their response to hack cues, and check whether hacking develops more slowly. This would test whether the units drive the learning or only track it.

If dopamine units do predict hacking, they could serve as an early warning signal during RL training. If a hack produces a reward response that never fades, that would also suggest a specific fix: change the training signal so the hack reward can be predicted away, as normal rewards are.

**Related projects:** [whether LLMs do distributional RL](#distributional-rl), [how LLMs represent goals](#goal-representations), [model organisms of RL from pretraining](#rl-pretraining-model-organisms), and [does Dynamic Fine-Tuning reduce emergent misalignment](#dft-emergent-misalignment).
