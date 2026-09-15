# Safety implications of looped transformers

Looped transformers reuse a set of layers over multiple computation steps. [Reasoning with Latent Thoughts](https://arxiv.org/abs/2502.17416) shows how this can support reasoning with additional internal computation. As more reasoning happens in hidden states, we need to understand what this changes about monitoring and controlling a model.

[A Mechanistic Analysis of Looped Reasoning Language Models](https://arxiv.org/abs/2604.11791) already studies recurrent dynamics, convergence, and stages of computation. [Latent Chain-of-Thought?](https://arxiv.org/abs/2507.02199) also investigates what can be decoded from intermediate states. I want to build on these results to study the **safety implications** of the architecture.

For example, a safety intervention might work at one iteration and then be undone by later computation. A monitor trained at one loop depth might become unreliable when we give the model more compute. And if the reasoning is internal, a monitor that depends on a readable chain-of-thought may lose access to useful evidence.

We would use open looped models and controlled tasks to ask:

- Does increasing the loop budget change harmful behavior or the reliability of safety monitors?
- Do later iterations preserve, weaken, or undo a safety intervention?
- When is a one-time intervention sufficient, and when is repeated intervention needed?
- Can an internal monitor transfer across loop counts, tasks, and stages of computation?
- Can we recognize an unsafe trajectory early enough to stop or redirect it while preserving useful task performance?

Interpretability tools would help explain these outcomes. The main goal is to identify which safety assumptions continue to hold when models reason through repeated internal computation.
