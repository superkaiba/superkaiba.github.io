# Affine Anticipation

Generating an answer involves many nonlinear steps, but how much of its internal representation is already determined by the context? [Future Lens](https://arxiv.org/abs/2311.04897) studies anticipation of subsequent tokens; our work asks about a representation summarizing an entire answer.

I have some results showing that a linear map from the final context activation predicts much of the mean answer activation, described in [Affine Anticipation: LLM Answer Representations Are Largely Linearly Predictable from Context](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf). These forecasts can support behavioral readouts before generation.

The completed paper is the starting point for [predicting answer activations](#answer-activations), [studying fine-tuning changes](#affine-anticipation-followups) and [forecasting conversation dynamics](#conversation-dynamics).
