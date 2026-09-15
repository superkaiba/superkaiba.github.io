# How linear are LLM representations?

Work on [neural sentence trajectories](https://arxiv.org/abs/2311.04930), [layer-to-layer prediction](https://arxiv.org/abs/2303.09435) and [feature transfer between models](https://arxiv.org/abs/2506.06609) finds useful linear structure in different parts of language-model computation. These are different notions of linearity: a good fit between two layers need not remain useful when repeatedly applied across generated tokens.

It would be useful to characterize when simple transition models explain behavior, and when nonlinear or context-dependent dynamics are necessary. This could make tools from dynamical systems applicable to actual model computations.

- Compare linear and nonlinear maps across tokens, layers and models; identify which token types and directions they fail to predict.
- Roll fitted maps forward and decode, testing fixed, token-conditioned and context-dependent transitions.
- Compare prompt processing with generation, including off-policy and reasoning continuations, and test middle-layer state-space approximations.
- Track linearity and trajectory straightening across model scale, context length and pretraining.
- Test sensitivity to perturbations and evidence for chaotic dynamics, separating deterministic instability from sampling noise.
