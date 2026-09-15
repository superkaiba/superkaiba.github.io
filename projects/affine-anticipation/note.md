# Affine Anticipation

How much of an LLM's answer representation can we predict before the model generates the answer? Although generating an answer involves many nonlinear steps, the context may already contain a surprisingly direct signal about the answer's internal representation.

In [Affine Anticipation: LLM Answer Representations Are Largely Linearly Predictable from Context](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf), we study the relationship between the final context-token activation and the mean activation across the answer. We find that this relationship is largely linear, and that predicted activations can help forecast sycophancy, hallucination, and harmful compliance.

The paper is the starting point for the ongoing [Predicting answer activations from context](#answer-activations) project.
