# Contextualized pretraining for more robust alignment

[Source-reliability learning](https://arxiv.org/abs/2310.15047) and [inoculation prompting](https://arxiv.org/abs/2510.04340) suggest that the context surrounding training examples can affect how their information generalizes. The [Scientist AI proposal](https://lawzero.org/en/publication/scientist-ai-safe-design-not-desiring) also motivates giving models explicit information about the provenance and reliability of what they read.

I have some results showing that source attribution during fine-tuning can reduce misalignment on unrelated tasks, though the unwanted behavior can return when the training frame is reapplied. These [preliminary experiments](https://github.com/superkaiba/truthification_pretraining/blob/main/writeup/truthification_summary.pdf) provide a starting point.

It would be useful to test whether source attribution during pretraining creates better-separated representations and more robust behavior under later fine-tuning. The pretraining extension needs a carefully chosen scale.

- Compare meaningful source and reliability labels with arbitrary labels and unlabeled data.
- Measure how attribution changes persona, source and belief representations.
- Apply matched later fine-tuning and test whether alignment is more robust.
- Evaluate missing, misleading and unreliable source labels to identify what the model actually learns to trust.
