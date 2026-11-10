---
title: How much of an LLM's output comes from the context and how much from the weights?
status: Not started
order: 5.5
math: true
---

# How much of an LLM's output comes from the context and how much from the weights?

**TL;DR:** Split each prediction an LLM makes into the part it could make from its weights alone and the part that needs the context. Do this in two ways: in bits of predictive information, and mechanistically, by separating computation that stays at the current position from computation that reads other positions through attention. Then map how the split changes with layer, token type, task, context length, model size, training stage and post-training.

There is a lot of work on one special case: knowledge conflicts, where a fact in the prompt contradicts what the model learned. For example, [in retrieval-augmented settings the MLP knowledge is used little when a relevant context is present](https://arxiv.org/abs/2406.12824), and [the same attention heads can carry both context and parametric memory](https://arxiv.org/abs/2503.10996). These studies pick prompts where the two sources disagree about one fact. As far as I can tell, nobody has measured the split across ordinary text and ordinary behavior, where context and weights work together on every token.

**An information split.** For a target token $y$ with context $x$, measure the information the model's prediction carries, in bits, relative to a uniform guess over the vocabulary $V$. It splits exactly into two terms:

$$
\underbrace{\log_2 |V| + \log_2 p_\theta(y \mid x)}_{\text{total}}
= \underbrace{\log_2 |V| + \log_2 p_\theta(y \mid \varnothing)}_{\text{weights only}}
+ \underbrace{\log_2 \frac{p_\theta(y \mid x)}{p_\theta(y \mid \varnothing)}}_{\text{from context}},
$$

where $p_\theta(y \mid \varnothing)$ is the prediction with an empty context (only the start token). The second term is the pointwise mutual information between the context and the target under the model, and it can be negative. A finer version uses nested windows of the last $k$ tokens, $p_\theta(y \mid x_{t-k:t})$ for $k = 0, 1, 2, \dots$. Each step adds the information carried by one more token of context, which gives a curve of "how far back the model needs to look".

**A mechanistic split.** At the final position $t$, the residual stream is a sum of contributions. Some reach it only through computation at position $t$ (the embedding, MLPs, attention to itself). Others pass through attention to earlier positions at least once. Split each attention output into its part from $s = t$ and its part from $s \ne t$, then follow both parts to the logits with the layer norms and MLPs linearized, as in attribution graphs. The fraction of the target logit carried by the second kind of path is the mechanistic context share. A simpler check is to run the model with attention restricted to the current position from some layer onward, and measure what is lost.

**Initial directions:**

- **Corpus-wide numbers.** Compute both splits over a mix of text types: prose, code, dialogue, math, and factual question answering. Report the average context share and its spread.
- **By token type.** Compare function words, content words, the second piece of a word split over several tokens, names, numbers and closing brackets. My guess is that word pieces and brackets are almost all context, and the first token of a fact is mostly weights.
- **By layer.** Track the mechanistic context share layer by layer. Check whether early layers are mostly position-local and the context share peaks in the middle layers.
- **Scale and training.** Repeat across model sizes and across pretraining checkpoints. Larger models know more facts and are also better in-context learners, so it is not obvious which share grows.
- **Post-training and behavior.** Measure the same split for behavior instead of tokens, for example how much of a persona, a refusal or a stated value is set by the system prompt and how much by the weights. Compare base and chat models.

**Related projects:** [predicting answer activations from context](#answer-activations), [what is stored in the final context activation](#context-vector), [whether secrets are stored in attention values or the residual stream](#secrets-values-vs-residual), and [steering and patching the KV cache instead of the residual stream](#kv-steering).
