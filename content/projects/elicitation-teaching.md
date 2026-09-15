---
id: "P26"
title: "Mechanistic differences between elicitation and teaching"
area: "Training"
status: "In progress"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "A mechanistic understanding of elicitation vs teaching"
---

# Mechanistic differences between elicitation and teaching

Fine-tuning can improve performance in at least two different ways: it can teach a model something new, or make the model use a capability it already had. Those outcomes can look similar if we only measure the final score.

[Bits That Count: Quantifying and Predicting Capabilities of Language Models](https://icml.cc/virtual/2026/poster/61292) uses an information-theoretic approach to this distinction. [Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks](https://arxiv.org/abs/2311.12786) provides a complementary controlled setting for studying how fine-tuning changes access to capabilities.

I would like to connect these approaches: does elicitation versus teaching have a recognizable signature inside the model, and can that signature predict how training will generalize?

We would start from a controlled setting where the two regimes are well defined and differ in as few other ways as possible. Then we could compare:

- Changes in residual-stream representations.
- Which components or features change during training.
- Differences in gradients and how quickly they evolve.
- Whether the relevant information was already accessible before fine-tuning.

An in-context version might be a simpler first experiment before moving to weight updates.

The longer-term question is whether we can inspect a model, dataset, or training run and predict whether an improvement is likely to come from teaching or elicitation. That would help us understand what our training procedures are actually doing.
