# Which nonlinearities can a model do without?

[LayerNorm-removal experiments](https://arxiv.org/abs/2507.02559) show that GPT-2 models can recover much of their performance after normalization is replaced through fine-tuning. [Work on linearizing MLP computations](https://arxiv.org/html/2603.03459v2) also reports that selected feed-forward computations can be replaced cheaply, with substantial differences across architectures.

It would be useful to understand which nonlinear operations remain necessary for particular capabilities, especially in larger models with gated MLPs. This could make simplified models more useful for mechanistic analysis, while revealing where approximate linear descriptions fail.

- Replace activation functions, multiplicative MLP gates, and normalization separately, then in combination.
- Compare immediate removal with recovery through a fixed fine-tuning budget.
- Evaluate reasoning, factual recall, and behavior under unfamiliar inputs alongside language-modeling loss.
- Locate examples where a linear replacement fails and trace the responsible computation.
- Distinguish a genuinely linear input–output map from an architecture whose running time merely scales linearly with sequence length.
