---
title: Is cognitive dissonance in LLMs System 1 or System 2?
status: Not started
order: 31.75
math: true
---

# Is cognitive dissonance in LLMs System 1 or System 2?

**TL;DR:** LLMs can shift their stated attitudes toward positions they argued for earlier. In one study of GPT-4o, the shift got larger when the model was told it chose which side to argue. This resembles human cognitive dissonance. Test whether the effect comes from fast, automatic processing (System 1: the model's own text in context primes its later answers) or from deliberate processing (System 2: the model builds a justification for what it did). The two accounts predict opposite effects of turning thinking on.

[Lehr et al.](https://www.pnas.org/doi/10.1073/pnas.2501823122) ran the classic induced compliance paradigm on GPT-4o. GPT-4o wrote a positive or negative essay about Vladimir Putin and then rated him. Its rating moved toward the essay. It moved further when GPT-4o was told it could freely choose which essay to write. [Cummins, Elson and Hussey](https://doi.org/10.1073/pnas.2517912122) argued that the result needs neither cognition nor dissonance. In their reruns, the rating shifted with the essay's valence whether GPT-4o wrote the essay or the user supplied it, which points to the essay's presence in the context window. Lehr et al. [replied with new data](https://doi.org/10.1073/pnas.2518613122). The human benchmark is also less settled than it looks: in a [recent multilab replication](https://www.psychologicalscience.org/observer/multilab-replication-cognitive-dissonance), attitudes changed whether or not participants chose to write the essay.

Related consistency effects show up in other settings. [Kumaran et al.](https://arxiv.org/abs/2507.03120) find a choice-supportive bias in Gemma 3, GPT-4o and o1-preview: when a model can see its first answer, it is more confident in it and less likely to change it. [Wang and Koch](https://arxiv.org/abs/2607.21558) planted a position in the context and attributed it to the model, the user or another AI. Models adopted it far more often when it was framed as their own earlier judgment, and the possessive "your" drove much of this. [Qi and Lerman](https://arxiv.org/abs/2606.22633) study how models resolve conflict between a prior stance and a counter-claim, and they turned thinking mode off on purpose.

On the deliberate side, chains of thought often justify an answer the model already picked. [Arcuschin et al.](https://arxiv.org/abs/2503.08679) find models writing coherent arguments for answering "yes" to both "Is X bigger than Y?" and "Is Y bigger than X?" [Probes can detect this kind of motivated reasoning](https://arxiv.org/abs/2603.17199) from activations before the reasoning is written, and [reasoning traces can continue after the model has committed to an answer internally](https://arxiv.org/abs/2605.11746).

Human psychology has two accounts that connect these. Kahneman describes System 2 as often endorsing the conclusions of System 1 instead of checking them. In the [associative-propositional evaluation model](https://doi.org/10.1037/0033-2909.132.5.692), associative processes have no notion of truth, and consistency is checked by propositional reasoning. On that view, dissonance reduction is a System 2 process. As far as I can tell, nobody has tested which account fits LLMs. The studies above used non-reasoning models, switched thinking off, or compared separate models without varying thinking within one model.

**Setup.** Let $A_0$ be the model's rating of the target in a fresh context, and $A$ its rating after writing the essay. Write $\Delta = A - A_0$. For a condition $c$, the dissonance effect is the gap between positive and negative essays:

$$
D_c = \mathbb{E}[\Delta \mid \text{positive essay}, c] - \mathbb{E}[\Delta \mid \text{negative essay}, c].
$$

Three contrasts then separate the accounts:

- **Choice:** $M = D_{\text{choice}} - D_{\text{no choice}}$. Lehr et al. found $M > 0$ for GPT-4o.
- **Attribution:** $S = D_{\text{self}} - D_{\text{other}}$, with the same essay text presented as the model's own or as someone else's. Priming by the text alone predicts $S \approx 0$. A self-consistency process predicts $S > 0$. Cummins et al. found no effect of authorship for GPT-4o without thinking, which fits $S \approx 0$.
- **Thinking:** $T = D_{\text{think}} - D_{\text{no think}}$, using the same weights with thinking switched on or off.

If the effect is System 1 priming, I would expect $T < 0$, since reasoning gives the model a chance to recall its baseline view, and $S \approx 0$ with or without thinking. If dissonance reduction is a System 2 process, I would expect $T > 0$, since reasoning gives the model room to build a case for its earlier behavior. I would also expect authorship to start mattering once the model can reason about it, so $S_{\text{think}} > S_{\text{no think}} \approx 0$. That interaction is the cleanest test, because the existing no-thinking result already sets the baseline.

**Initial directions:**

- **Replicate with thinking on and off.** Use open hybrid models where thinking can be switched on and off with the same weights, plus closed models with adjustable reasoning budgets. Use several attitude targets, including less politically loaded ones, so refusals and safety training matter less.
- **Hold the essay text fixed.** Reuse each essay the model wrote across self, user and other-AI attribution, so only the attribution changes. Run every attribution condition with thinking on and off to estimate the interaction above.
- **Read the reasoning traces.** When thinking is on, check whether the trace mentions the earlier essay, argues for its position, or recalls a prior view. Resample from points in the trace to test which parts change the final rating.
- **Track the attitude internally.** On open models, train a probe for the attitude toward the target. Measure when it moves: while the essay is written, during the reasoning trace, or only at the rating. Movement during writing fits System 1. Movement during the trace fits System 2.
- **Vary the distance in context.** Insert unrelated turns between the essay and the rating. One of my hypotheses is that models run more on autopilot later in a long context. If so, the drift without thinking might persist or grow with distance, while thinking might reduce it.
- **Compare with humans carefully.** Report effect sizes next to the multilab replication results, since the human choice effect is itself uncertain.

**Related projects:** [is the chain of thought caught between the talker and the doer?](#cot-between-talker-doer), [inside and outside J-space: System 1 and System 2 thinking](#j-space-system-thinking), [how much of an LLM's behavior is decided in advance?](#behavior-commitment), and [does reasoning change what a model believes about itself?](#reasoning-self-beliefs).
