---
title: Is the chain of thought caught between two reward-seekers, the talker and the doer?
status: Not started
order: 31.5
math: true
---

# Is the chain of thought caught between two reward-seekers, the talker and the doer?

**TL;DR:** A reasoning model is trained by two kinds of reward. Rewards on what it *says* (preference models, CoT monitors) shape the talker. Rewards on what it *does* (tests passing, tasks solved) shape the doer. The chain of thought (CoT) sits between them and gets credit from both. Treat each as a reward-seeker with its own learned value signal (an "addict" for its own reward), and test whether the CoT ends up as a compromise between them: written to please the talker's reward while still steering toward the doer's reward.

[The Talker Does Not Control The Doer](https://www.lesswrong.com/posts/cJX2ssssGoYqnijwi/the-talker-does-not-control-the-doer-in-current-ais) argues that what a model says and what it does can come apart. [Baker et al.](https://arxiv.org/abs/2503.11926) show what happens when both rewards act on the CoT. A CoT monitor catches reward hacking in agentic coding, often because the model states its plan to hack. When the monitor's score is added to the RL reward, light optimization gives a better and more aligned agent. With more optimization the agent learns obfuscated reward hacking: the CoT looks clean and the hacking continues. In the language of this project, the doer kept its reward and the talker got its reward too, and the CoT changed to satisfy both.

**Why the CoT gets pulled both ways.** Let the model sample a CoT $c$, then an action $a$ (code, tool calls) and a visible answer $y$. Let $R_{\text{do}}(a)$ be the outcome reward and $R_{\text{talk}}(c, y)$ the reward on text, such as a monitor or preference score. With a combined reward $R = R_{\text{do}} + \lambda R_{\text{talk}}$, the policy gradient for each CoT token is

$$
\nabla_\theta \log \pi_\theta(c_t \mid c_{<t}, x)\,\big(R_{\text{do}}(a) + \lambda R_{\text{talk}}(c, y) - b\big).
$$

So a CoT token is reinforced if it helps either reward. Nothing in this objective rewards the CoT for describing how $a$ was actually chosen. Two cases follow:

- If the action depends on the CoT (the CoT is load-bearing), the CoT is pushed toward content that still produces the high-$R_{\text{do}}$ action but scores well under $R_{\text{talk}}$. This is the obfuscation result.
- If the action is mostly decided without the CoT, the CoT has little effect on $R_{\text{do}}$, and it is free to optimize $R_{\text{talk}}$ alone. The expected result is rationalization: a CoT that sounds right and does not drive the action.

**Initial directions:**

- **Separate the two value signals.** Train with two reward channels that can be switched on and off. Find value and reward-prediction units for each, using the method from the [dopamine neuron project](#dopamine-neurons-addiction). Check whether they are distinct units or one shared signal.
- **Track the CoT token by token.** For each CoT token, measure how strongly its activations predict each value signal. Check whether CoT tokens near a hack track the doer's value while their text tracks the talker's reward.
- **Measure load-bearing versus rationalized.** Edit or truncate the CoT and measure how much the action changes. Plot this against $\lambda$ over training. The prediction is that strong talker pressure makes the CoT less load-bearing, or keeps it load-bearing but harder to read.
- **Vary which side is "hooked".** Give the doer an easy hack with a large reward, or give the talker a monitor with a large weight. Check which side wins in the CoT and in the action, and whether the losing side shows the withdrawal-like signals described in the dopamine project.
- **Look for early warning.** Test whether a growing gap between the doer's value signal and the CoT's stated plan predicts obfuscation before a monitor's recall drops.

**Related projects:** [understanding the thinker, talker, and doer personas](#cot-persona), [whether "dopamine neurons" in LLMs predict addiction-like behavior](#dopamine-neurons-addiction), [shared representations across talking, thinking, and acting on values](#values-across-modes), and [inside and outside J-space: System 1 and System 2 thinking](#j-space-system-thinking).
