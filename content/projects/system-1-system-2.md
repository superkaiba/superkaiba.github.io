---
title: Exploring System 2 and System 1 thinking as a model of LLM behavior
status: Fleshed out
order: 32.3
math: true
aliases: [j-space-system-thinking, dissonance-system-thinking]
---

# Exploring System 2 and System 1 thinking as a model of LLM behavior

People often seem to be surprised when models take actions or have thoughts which are not aligned or even contradictory with how they talk to us or represent themselves ([Turpin et al., 2023](https://arxiv.org/abs/2305.04388); [Chen et al., 2025](https://arxiv.org/abs/2505.05410); [Arcuschin et al., 2025](https://arxiv.org/abs/2503.08679)). I think we can map this to system 2 vs system 1 thinking in humans (Kahneman, 2011; [Evans & Stanovich, 2013](https://doi.org/10.1177/1745691612460685)).

Although we try to train the models to reason about each action they take (i.e. system 2 thinking) and then follow their reasoning, it seems clear that a lot of their behavior can be seen as more "reflexive"/system 1, especially when reward is involved ([Baker et al., 2025](https://arxiv.org/abs/2503.11926); [Mirtaheri & Belkin, 2026](https://arxiv.org/abs/2603.17199)).

In psychology/cognitive science, system 2 is often viewed as an "endorser" of system 1's conclusions rather than a critic (Kahneman, 2011; [Haidt, 2001](https://doi.org/10.1037/0033-295X.108.4.814); [Mercier & Sperber, 2011](https://pubmed.ncbi.nlm.nih.gov/21447233/)), which would explain the motivated reasoning seen in modern LLMs ([Lindsey et al., 2025](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)).

The goal of this project would first be to see if this system 1 vs system 2 account holds for LLMs.

- I think system 1 can be seen as the "autocomplete"/"in-context learning" learned in pretraining ([Olsson et al., 2022](https://arxiv.org/abs/2209.11895); [Venhoff et al., 2025](https://arxiv.org/abs/2510.07364); [Marks et al., 2026](https://alignment.anthropic.com/2026/psm)).
- System 2 is mostly present in the CoT, but can be seen as mostly switching between different autocomplete modes/personas ([Kim et al., 2026](https://arxiv.org/abs/2601.10825)) using certain key "switch words" (wait! actually!) ([Qian et al., 2025](https://arxiv.org/abs/2506.02867); [Tsui, 2025](https://arxiv.org/abs/2507.02778)).
- I think this can be linked to entropy neurons ([Stolfo et al., 2024](https://arxiv.org/abs/2406.16254)).
    - If the model is "certain" about the continuation then it will continue to use system 1. If it is highly uncertain then it will activate system 2, which will cause a "switch word" and force it to take a different perspective ([Wang et al., 2025](https://arxiv.org/abs/2506.01939)). This matches models of when humans switch to system 2 ([Thompson et al., 2011](https://doi.org/10.1016/j.cogpsych.2011.06.001); [De Neys, 2023](https://doi.org/10.1017/S0140525X2200142X)).

If this picture holds, I think it already gives an interesting and illuminating perspective on LLM behavior, but one potential followup would be to explore directly externalizing the system 2 to a different model (probably with different post training) which can allow it to critique the model's reasoning in a more unbiased way ([Huang et al., 2023](https://arxiv.org/abs/2310.01798); [Tsui, 2025](https://arxiv.org/abs/2507.02778); [Panickssery et al., 2024](https://arxiv.org/abs/2404.13076)). This is similar to proposals around debate ([Irving et al., 2018](https://arxiv.org/abs/1805.00899); [Khan et al., 2024](https://proceedings.mlr.press/v235/khan24a.html)).

### Inside and outside J-space

[Verbalizable Representations Form a Global Workspace in Language Models](https://www.transformer-circuits.pub/2026/workspace/index.html) identifies J-space representations that support verbal report and flexible internal reasoning, while some routine processing can proceed without them (its analysis of features outside J-space finds examples involving syntax and formatting). One way to test the system 1 vs system 2 picture is to ask whether processing outside J-space supports an automatic "doer", and when deliberate reasoning changes what it does. J-space is a sparse set of representations, so its remainder is not a fixed orthogonal subspace, and answering without written reasoning need not mean bypassing J-space.

- Characterize features inside J-space and in the remaining activations across layers, tasks and models.
- Compare routine tasks with matched tasks that require reporting or flexibly using the same information, and ablate or patch each component to test its causal role.
- Study action selection when a model's stated intention conflicts with its behavior, testing which representations influence the final action.
- Use [System 2-to-System 1 distillation](https://arxiv.org/abs/2407.06023) to test whether learned skills become less dependent on J-space as they become more automatic.

### Cognitive dissonance as a test case

LLMs can shift their stated attitudes toward positions they argued for earlier. [Lehr et al.](https://www.pnas.org/doi/10.1073/pnas.2501823122) had GPT-4o write a positive or negative essay about Vladimir Putin and then rate him. The rating moved toward the essay, and moved further when GPT-4o was told it freely chose which essay to write. [Cummins, Elson and Hussey](https://doi.org/10.1073/pnas.2517912122) found the rating shifted the same way when the user supplied the essay, which points to the essay's presence in context. Lehr et al. [replied with new data](https://doi.org/10.1073/pnas.2518613122). The human benchmark is also unsettled: in a [multilab replication](https://www.psychologicalscience.org/observer/multilab-replication-cognitive-dissonance), attitudes changed whether or not participants chose to write the essay.

Related consistency effects appear elsewhere. [Kumaran et al.](https://arxiv.org/abs/2507.03120) find a choice-supportive bias: a model that can see its first answer is more confident in it and less likely to change it. [Wang and Koch](https://arxiv.org/abs/2607.21558) find models adopt a planted position far more often when it is framed as their own earlier judgment. These studies used non-reasoning models or switched thinking off, so they do not say which system drives the effect.

The two accounts predict opposite effects of thinking. If the effect is System 1 priming, the model's own text in context drives the later answer, and reasoning should give it a chance to recall its baseline view. If it is System 2, reasoning gives the model room to build a case for what it already did. In the [associative-propositional evaluation model](https://doi.org/10.1037/0033-2909.132.5.692), consistency is checked by propositional reasoning, which fits the second account.

Let $A_0$ be the model's rating of the target in a fresh context, and $A$ its rating after writing the essay. Write $\Delta = A - A_0$. For a condition $c$, the dissonance effect is

$$
D_c = \mathbb{E}[\Delta \mid \text{positive essay}, c] - \mathbb{E}[\Delta \mid \text{negative essay}, c].
$$

Two contrasts separate the accounts. Authorship: $S = D_{\text{self}} - D_{\text{other}}$, with the same essay shown as the model's own or as someone else's. Thinking: $T = D_{\text{think}} - D_{\text{no think}}$, with the same weights and thinking switched on or off. System 1 priming predicts $T < 0$ and $S \approx 0$ with or without thinking. System 2 justification predicts $T > 0$ and $S_{\text{think}} > S_{\text{no think}} \approx 0$. That interaction is the cleanest test, because the existing no-thinking result already sets the baseline.

- Replicate the essay paradigm on open hybrid models with thinking on and off, plus closed models with adjustable reasoning budgets. Use several less politically loaded targets, so refusals matter less.
- Reuse each essay the model wrote across self, user and other-AI attribution, so only the attribution changes.
- With thinking on, check whether the trace mentions the essay, argues for its position, or recalls a prior view. Resample from points in the trace to see which parts change the rating.
- On open models, probe for the attitude and measure when it moves: while the essay is written (System 1) or during the reasoning trace (System 2).
- Insert unrelated turns between the essay and the rating, to test whether drift without thinking persists or grows with distance.
