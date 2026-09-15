# Do models represent whether text is AI-generated?

Humans sometimes recognize a piece of writing as “AI-generated,” even when they cannot point to one specific phrase that gives it away. I wonder whether language models also represent this distinction internally.

[Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts](https://arxiv.org/abs/2306.04723) uses representation geometry to detect generated text. Separately, [LLM Evaluators Recognize and Favor Their Own Generations](https://arxiv.org/abs/2404.13076) and [The human-authorship halo](https://arxiv.org/abs/2510.08831) show why perceived authorship can matter for evaluation.

I want to connect these observations: can we find an internal representation of the perceived author, and does changing that representation change how the model evaluates or trusts the text?

We would compare human-written and model-generated passages while matching topic, length, and formatting as closely as possible. We could also tell the model that a passage was written by a human or an AI and see whether that changes the representation.

Some questions:

- Can a probe generalize to text from model families it has never seen?
- Is it detecting authorship, or just a style common in the training examples?
- Does believing that text is AI-generated change how much the model trusts it?
- What happens when the actual source and the stated source disagree?
