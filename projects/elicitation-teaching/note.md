# Mechanistic differences between elicitation and teaching

Fine-tuning can improve performance in at least two different ways: it can teach a model something new, or make the model use a capability it already had. Those outcomes can look similar if we only measure the final score.

[This work on elicitation versus teaching](https://openreview.net/pdf?id=re9NtTb1Dy) uses an information-theoretic approach to distinguish them. I would like to understand whether that distinction also has a recognizable signature inside the model.

We would start from a controlled setting where the two regimes are well defined and differ in as few other ways as possible. Then we could compare:

- Changes in residual-stream representations.
- Which components or features change during training.
- Differences in gradients and how quickly they evolve.
- Whether the relevant information was already accessible before fine-tuning.

An in-context version might be a simpler first experiment before moving to weight updates.

The longer-term question is whether we can inspect a model, dataset, or training run and predict whether an improvement is likely to come from teaching or elicitation. That would help us understand what our training procedures are actually doing.
