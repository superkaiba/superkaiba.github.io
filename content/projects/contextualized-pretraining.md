---
id: "P27"
title: "Contextualized pretraining for more robust alignment"
area: "Training"
status: "In progress — scope to confirm"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Contextualized pretraining"
---

# Contextualized pretraining for more robust alignment

During ordinary pretraining, a model sees text from many sources, but it may receive little explicit information about who wrote a document or how reliable it is. One hypothesis is that this makes it harder to keep different perspectives and personas separate.

[LawZero's Scientist AI proposal](https://lawzero.org/en/publication/scientist-ai-safe-design-not-desiring) motivates giving models more context about their training data. This is also related to [inoculation prompting](https://arxiv.org/abs/2510.04340), where the context surrounding training examples can influence how their behavior generalizes.

[Implicit meta-learning may lead language models to trust more reliable sources](https://arxiv.org/abs/2310.15047) already connects source reliability during training to later learning. [Synthetic Persona Pretraining](https://arxiv.org/abs/2608.13482) studies installing personas early in training. These make reliability attribution and early persona formation useful baselines for the project.

I propose to test source and reliability attribution during language-model pretraining. The hypothesis is that this could produce a more clearly separated persona space and make the assistant less vulnerable to later misalignment-inducing fine-tuning.

We would check:

- Does adding source information change the geometry of learned representations?
- Does alignment become more robust under later fine-tuning?
- Is the benefit specific to meaningful attribution, or can arbitrary labels produce it?
- What happens when source labels are missing, misleading, or unreliable?

My [preliminary fine-tuning experiments](https://github.com/superkaiba/truthification_pretraining/blob/main/writeup/truthification_summary.pdf) provide an initial setting for testing attribution. Moving to pretraining will require a carefully scoped experiment and substantially more compute.
