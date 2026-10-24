---
title: How few parameters does RLVR need when reusing a pretrained module?
status: Not started
order: 54.5
---

# How few parameters does RLVR need when reusing a pretrained module?

**TL;DR:** Freeze a language model and an existing pretrained external module, then test how much reinforcement learning with verifiable rewards (RLVR) can achieve by training only a tiny controller that combines their outputs.

[TinyLoRA](https://arxiv.org/abs/2602.04118) shows that very small learned updates can produce strong RLVR gains in its tested settings. [Universal Reasoner](https://proceedings.mlr.press/v306/kim26f.html) trains a separate reasoning module with verifiable rewards and combines its output logits with those of a frozen backbone. These results raise a narrower question: if both models already contain useful computation, how many new parameters are needed to learn when and how strongly to use it?

I want to compare spending a small trainable parameter budget on controlling a frozen pretrained module with spending the same budget on adapting the main model. Both models would read the same prompt and generated prefix. A controller would set the external model's contribution to the next-token scores, using features such as uncertainty, disagreement between the models, and token position. Start with one learned constant weight, then test small state-dependent controllers with tens or hundreds of trainable scalars.

External modules and expert routing already have relevant prior work. [Hard-Routed Mixtures of Reasoning LoRAs](https://arxiv.org/abs/2606.31413) composes frozen experts while training a router and an attention LoRA. The proposed test keeps both the backbone and external module frozen throughout RLVR and measures what learning only the controller adds. The resulting minimum would depend on the checkpoints, tasks, and performance target, rather than establish a universal parameter requirement.

**Initial directions:**

- **Measure the parameter curve.** Compare one constant weight with controllers containing 13, 49, and 196 total trainable scalars. Count all learned biases and scales, and compare with TinyLoRA at matching budgets.
- **Separate learned control from fixed combination.** Include each model alone, validation-tuned logit combination, and temperature controls. Test whether a state-dependent controller improves on the best fixed rule.
- **Test the value of existing expertise.** Compare a general instruction model with an already trained reasoning specialist of similar size. Record each module's training provenance. If a module is trained specifically for this study, account for that training separately.
- **Check generalization.** Begin with verifiable math tasks, using separate training, validation, and test sets. Include fresh generated problems with held-out families, multiple training seeds, and uncertainty estimates.
- **Measure the actual cost.** Report total resident parameters, training GPU hours, memory, answer length, and inference latency alongside trainable parameters. Compare against additional main-model sampling at matched inference cost.
- **Identify the limits.** Check vocabulary and token compatibility before combining outputs. If tiny controllers fail, test a larger controller to distinguish limited control capacity from an unhelpful module. If fixed combination works just as well, report that the tested gain requires little or no new RL adaptation.

**Related projects:** [Comparing prompting, steering, LoRA, and fine-tuning](#adaptation-methods), [mechanistic differences between elicitation and teaching](#elicitation-teaching), and [localizing the assistant persona to an external module](#assistant-persona-module).
