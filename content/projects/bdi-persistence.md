---
title: How long do an LLM's beliefs, goals and intentions persist?
status: Not started
order: 13.7
math: true
---

# How long do an LLM's beliefs, goals and intentions persist?

**TL;DR:** Use the belief-desire-intention (BDI) model of agents as a template for LLM internals. Measure how long a belief, a goal and a planned token stay readable in the residual stream, and whether later tokens read the stored decision or recompute it from the original cue.

In the [BDI model](https://users.cs.utah.edu/~tch/notes/refs/Rao-Georgeff1995.pdf), an agent keeps beliefs about the world, goals it would like to reach, and intentions it has committed to. Following Bratman, commitment is what makes intentions useful: an agent with limited computation can reuse an earlier decision instead of recomputing it at every step. The cost is that it can keep pursuing a plan after the plan stops making sense. [Kinny and Georgeff](https://mlanthology.org/ijcai/1991/kinny1991ijcai-commitment) found that agents which rarely reconsider their intentions do better when the world changes slowly, and agents which reconsider often do better when it changes fast.

Each of these parts has some evidence in LLMs, measured separately and with different methods. Transformers trained on hidden Markov processes [linearly represent the optimal belief states](https://arxiv.org/abs/2405.15943) in their residual stream. Claude 3.5 Haiku [selects a rhyme word at the newline](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) before writing the line that ends with it. [Where's the Plan?](https://arxiv.org/abs/2605.07984) finds that Qwen3, Gemma-3 and Llama-3 models all encode the future rhyme at the line boundary, but only Gemma-3-27B causally relies on that encoding. For goals, [instruction drift appears within eight rounds](https://arxiv.org/abs/2402.10962) of self-chat and is linked to attention decay, and [goal drift in LM agents](https://arxiv.org/abs/2505.02709) grows with the agents' tendency to pattern-match as the context gets longer.

A transformer has no recurrent state between tokens apart from the KV cache. So a belief or intention that persists can be implemented in two ways. The model can carry it: write the decision at one position and read it through attention at later positions. Or it can re-derive it: recompute the decision from the original cue at each later position. Only the first matches commitment in Bratman's sense, and behavior alone cannot tell the two apart. I have not found a study that measures all three BDI components in the same model with the same method.

**Persistence time.** Set a value $v$ at position $n$ (a fact, a goal, or a planned word). Train a probe $g$ on the residual stream $h^{n}_{\ell}$ at layer $\ell$, then apply the same probe $d$ tokens later:

$$
P(d) = \mathrm{Pr}\big[g(h^{n+d}_{\ell}) = v\big], \qquad P(d) - c \approx A\, e^{-d/\tau},
$$

where $c$ is chance accuracy. Taking logs gives a straight line in $d$ with slope $-1/\tau$, so $\tau$ is a persistence time in tokens. An ideal BDI agent has a flat curve until an event that should end the commitment, such as contradicting evidence, an authorized change of goal, or emitting the planned word.

**Carried fraction.** Pair each prompt with a counterfactual of the same length that sets a different value. In a site patch, keep the clean input and replace the activations at the decision site with the counterfactual ones. In a cue patch, use the counterfactual input and restore the clean activations at the decision site. If $E_{\text{site}}$ and $E_{\text{cue}}$ are the rates at which the output follows the counterfactual under each patch, then

$$
R = \frac{E_{\text{site}}}{E_{\text{site}} + E_{\text{cue}}}
$$

is close to 1 when later tokens read the stored decision and close to 0 when they recompute it from the cue.

**Initial directions:**

- **Build matched tasks for each component.** For beliefs, state a fact once ("Sam put the key in the red box"). For goals, set one in the system prompt. For intentions, use rhyming couplets or code where the model plans a later token. Then vary what follows: irrelevant filler, a distractor (a misleading hint, a user nudging toward a competing goal, an aside inserted mid-line), or relevant evidence (Sam moves the key, the operator changes the goal, the planned word is banned).
- **Measure persistence curves.** Fit $\tau$ for each component and condition. Use a probe trained at the decision site and also probes retrained at each distance. If the fixed probe decays while retrained probes do not, the information survives but its encoding changes. Report the full curves, and fit a decay time only where an exponential fits.
- **Measure the carried fraction.** Patch the decision site at every layer's input, so its keys and values change at every depth. The decision site must be a different position from the cue, such as the newline after the word to rhyme with. Positions between the cue and the site can also carry the value, so sweep the patched span and report how $R$ changes.
- **Test the BDI predictions directly.** A BDI agent keeps a belief or plan through filler and distractors and updates it on relevant evidence. Count both failure types: dropping a commitment after irrelevant text, and keeping it after evidence that should end it.
- **Compare base and instruction-tuned models.** [Detecting and Characterizing Planning](https://arxiv.org/abs/2508.18098) finds that instruction tuning refines plan selection in Gemma-2-2B. Test whether post-training also changes $\tau$ and $R$. Include several sizes from one family, since only the largest Gemma-3 model used its rhyme plan.
- **Connect to drift in long contexts.** Test whether $\tau$ and $R$ measured on short controlled tasks predict behavioral goal drift in long agentic transcripts.

A useful result would be a table of persistence times and carried fractions for beliefs, goals and intentions across a few models. It would show which parts of a BDI-style description of LLMs correspond to mechanisms inside the model, and which only describe its behavior.

**Related projects:** [How much of an LLM's behavior is decided in advance?](#behavior-commitment), [layerwise belief updating](#layerwise-belief-updating), [whether models update beliefs from internal states or earlier answers](#internal-beliefs-vs-written-answers), and [personas as persistent features](#persistent-personas), which measures persistence for persona directions.
