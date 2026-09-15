# Affine Anticipation

How much of an LLM's answer representation can we predict before the model generates the answer? Although generating an answer involves many nonlinear steps, the context may already contain a surprisingly direct signal about the answer's internal representation.

In [Affine Anticipation: LLM Answer Representations Are Largely Linearly Predictable from Context](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf), we study the relationship between the final context-token activation and the mean activation across the answer. We find that this relationship is largely linear, and that predicted activations can help forecast sycophancy, hallucination, and harmful compliance.

This connects to [Future Lens](https://arxiv.org/abs/2311.04897), which anticipates subsequent tokens from a hidden state, and [ParaScopes](https://arxiv.org/abs/2511.00180), which studies information about future text in model activations. Our target is the model's own mean answer representation, allowing us to apply answer-space behavioral readouts before generating the answer.

The paper is the starting point for [Predicting answer activations from context](#answer-activations) and the separate [Follow-ups to Affine Anticipation](#affine-anticipation-followups) project.
