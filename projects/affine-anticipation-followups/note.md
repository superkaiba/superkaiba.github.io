# Understanding fine-tuning through context-to-answer metamodels

**TL;DR:** Compare compact models of how context shapes answers before and after fine-tuning to understand—and potentially predict—how training changes behavior across situations.

[My recent paper on linear context-answer relationships](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) introduces context-to-answer metamodels: compact models that predict answer activations from context. I have some results showing that a learned linear map from the final context token's activation can predict the mean activation across the answer's tokens before generation, and that this relationship changes during supervised fine-tuning. My work on [Delta-Crosscoder](https://arxiv.org/abs/2603.04426) also examines features that change during fine-tuning.

This project proposes to study fine-tuning by comparing these compact maps before and after training. The aim is to understand how training changes behavior in different contexts, including when alignment generalizes and when narrow training produces broader misalignment.

**First Steps**

- Fit metamodels before and after fine-tuning on datasets targeting different behaviors; begin with individual batches to isolate their effects.
- Test whether map changes predict held-out behavior, emergent misalignment, and context-dependent misalignment.
- Compare supervised fine-tuning and reinforcement learning, controlling for changes of representation coordinates.
- Test whether information about the training data predicts the map changes before updating the model, and use interventions to investigate their causal role.
