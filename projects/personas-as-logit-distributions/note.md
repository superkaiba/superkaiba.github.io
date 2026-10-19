# Defining and characterizing personas as distributions over logits

**TL;DR:** Define personas through their distributions over logits, then test whether these distributions capture stable behavioral differences across contexts and support predictable control of generation.

[PICLe](https://proceedings.mlr.press/v235/choi24e.html) models an LLM as a mixture of persona-specific output distributions. [Fundamental Limitations of Alignment](https://proceedings.mlr.press/v235/wolf24a.html) studies how prompts reweight behavioral components of a language-model distribution. At the output layer, [Steer Model beyond Assistant](https://arxiv.org/abs/2601.06403) amplifies the difference between persona-conditioned and default logits, while [DExperts](https://aclanthology.org/2021.acl-long.522/) combines expert and anti-expert logits to control attributes such as sentiment. These provide related formulations without establishing that a persona is a probability distribution over logit vectors.

The first step is to distinguish a persona-conditioned token distribution, $p_\phi(y\mid x)=\operatorname{softmax}(z_\phi(x))_y$, from a distribution over the logit vectors themselves:

$$z\sim q_\phi(z\mid x),\qquad y\sim\operatorname{Categorical}(\operatorname{softmax}(z)).$$

Here, $x$ is the shared task context and $\phi$ is the persona. With fixed weights and an exact input, a standard deterministic forward pass gives one logit vector. A distribution over vectors therefore needs a specified source of variation, such as equivalent persona prompts or latent persona subtypes. Variation across task contexts should be measured separately so that topic differences do not masquerade as character.

It would be useful to characterize what stays consistent within a persona, how personas differ or overlap, and whether a distribution adds predictive value beyond a mean logit shift. This is an open research direction, not a claim that the formulation is novel or already validated.

**First Steps**

- Collect logits for several personas across shared tasks, persona-prompt paraphrases, and matched continuation prefixes. Hold the model, tokenizer, and temperature fixed. Compare raw logits with changes relative to a neutral prompt.
- Remove the arbitrary common offset in each logit vector by centering it, or use log-probability ratios. Compare variation within and between personas while controlling for wording, topic, and answer format.
- Fit simple distributions over logit shifts and compare them with a mean shift, persona-conditioned token distributions, and activation-based persona representations. Test whether distributional features improve persona identification and prediction of held-out behavior across new tasks.
- Test persona composition and interpolation. Distinguish averaging token probabilities from averaging logits, which generally produce different distributions, and specify whether a latent persona is sampled once per conversation or repeatedly during generation.
- Intervene using the fitted distributions and measure trait expression, consistency over long contexts, generation quality, and unrelated capabilities. A descriptive separation between personas would not by itself establish a causal mechanism or useful control method.

This complements [persona selection as Bayesian inference](#bayesian-personas) and [nonlinear geometry of persona representations](#persona-manifolds) by asking what a persona is at the model's output interface.
