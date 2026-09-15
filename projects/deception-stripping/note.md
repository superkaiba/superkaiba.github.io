# Distillation for deception stripping

One important problem in AI safety is figuring out what hidden behaviors or goals a model has. [Subliminal learning](https://arxiv.org/abs/2507.14805) shows that traits can transfer between models through distillation even when the training text does not visibly express those traits.

To successfully conceal a behavior, a model needs both to have the behavior and to keep it hidden. Our hypothesis is that these two things may not transfer equally well to a smaller student model.

I propose to take a model with a known hidden behavior, distill it into a smaller model, and test whether the student inherits the behavior without inheriting the same ability to conceal it. [AuditBench](https://arxiv.org/abs/2602.22755) and [password-locked models](https://arxiv.org/abs/2405.19550) provide possible controlled settings.

We already have preliminary results in some settings. The project would expand those results and investigate:

- When does the hidden behavior transfer?
- When does concealment transfer with it?
- How do model size, model family, and the distillation method affect the outcome?
- Does the method reveal information that ordinary elicitation misses?
- What explains cases where the behavior disappears entirely?

The distinction between revealing a behavior and simply destroying it is central to the project.
