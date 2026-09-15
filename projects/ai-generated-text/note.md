# Do models represent whether text is AI-generated?

Humans sometimes recognize a piece of writing as “AI-generated,” even when they cannot point to one specific phrase that gives it away. I wonder whether language models also represent this distinction internally.

[Work on detecting generated text through the geometry of representations](https://arxiv.org/abs/2306.04723) provides one starting point. The question here is whether we can find a representation that tracks the perceived author, and whether that representation affects how the model responds to the text.

We would compare human-written and model-generated passages while matching topic, length, and formatting as closely as possible. We could also tell the model that a passage was written by a human or an AI and see whether that changes the representation.

Some questions:

- Can a probe generalize to text from model families it has never seen?
- Is it detecting authorship, or just a style common in the training examples?
- Does believing that text is AI-generated change how much the model trusts it?
- What happens when the actual source and the stated source disagree?
