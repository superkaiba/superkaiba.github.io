# What is stored in the final context activation?

[In-context task vectors](https://arxiv.org/abs/2310.15916) and [Affine Anticipation](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) suggest that a context activation can contain information about both the requested task and the answer the model is about to give. This makes it a useful place to ask what has already been decided before generation begins.

It would be useful to separate prompt information, task information and prospective answer information, and understand what additional computation creates each of them. Being able to read something out does not establish that the model uses it.

- Apply a logit lens to individual, mean-pooled and max-pooled activations, tracking how readouts change across layers.
- Use matched prompts to separate facts, task identity, user information and intended behavior.
- Measure what information each additional layer or token contributes, then test its role with interventions.
- Track how the final context vector changes over a conversation, including changes that precede a shift in behavior.
