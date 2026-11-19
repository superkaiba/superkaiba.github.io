# Predicting answer activations from context

This project is complete. Tommy He and I wrote it up as [Context–Answer Metamodels: Forecasting LLM Activations Before the First Answer Token](https://tommyhe.com/asset/context-answer-metamodels.pdf) (NeurIPS 2026 NeuralArtifacts Workshop, oral spotlight; [code](https://github.com/Tufalabs/context-answer-metamodels)). We forecast the mean and variability of answer activations from prompt activations before generation. The forecasts keep behavioral signal, improve with more training data, and transfer across tasks and models.

[My recent paper on linear context-answer relationships](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) studies answer prediction before generation. I have some results showing that a learned linear map from the final context token's activation can predict the mean activation across the answer's tokens. On held-out Qwen2.5-7B-Instruct conversations, the linear map reaches R² = 0.81, compared with 0.86 for a nonlinear MLP. [Future Lens](https://arxiv.org/abs/2311.04897) studies a related possibility at the level of future tokens. A good average prediction can still miss the behavior we care about.

It would be useful to build on these results by understanding what is linearly predictable, what requires nonlinearity, and how much uncertainty comes from the model sampling different answers.

- Characterize the most and least predictable directions and the dimensionality of answer representations.
- Separate persistent behavioral information from token-specific variation and sampling noise from prediction error.
- Develop nonlinear predictors and distributional predictors of answer activations, testing whether they improve on linear prediction and capture the range of activations across sampled answers.
- Compare pooling across tokens and layers, and track predictability as an answer unfolds.
- Forecast a judge's verdict before and during generation, checking predictions against actual outputs.
- Test rare behaviors and reward hacking, paying particular attention to calibration and false negatives.
