# Follow-ups to Affine Anticipation

In my [newest paper, Affine Anticipation](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf), we find a linear map from context to answer representations. The paper includes initial comparisons across fine-tuning stages and between linear and nonlinear predictors. I would like to understand these relationships more deeply and test when the map supports causal predictions.

My work on [Delta-Crosscoder](https://arxiv.org/abs/2603.04426) studies fine-tuning-specific features and their behavioral effects. [Model stitching](https://arxiv.org/abs/2506.06609) provides a way to align representation spaces, helping us distinguish a change of coordinates from a change in behavior. [Local linear optimal control](https://arxiv.org/abs/2604.19018) also shows how local layerwise approximations can guide activation interventions; here we would investigate a map from the context to an entire answer.

Some directions to build on this:

- Understand how fine-tuning changes the map.
- Test whether changes in the map predict changes in behavior.
- Identify what the map predicts well and what actually requires nonlinearity.
- Find out when a good predictive approximation also gives a useful causal explanation.
