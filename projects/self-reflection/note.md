# Self-reflection to prevent reward hacking

**TLDR:** Test if reminders to reflect on the task's intended goal prevent reward hacking or cause rationalization, and examine the internal changes and performance trade-offs on difficult tasks

As LLMs are given increasingly difficult and long-running tasks, reward hacking has emerged as a big problem. Reward hacking incidents seem to occur most frequently in long-running tasks. [Goodfire's activation monitors](https://arxiv.org/abs/2609.19101) (Bergen et al., 2026) and [PRIME](https://arxiv.org/abs/2606.09711) (Beigi et al., 2026) identify internal signals associated with hacking, suggesting that models "know" when they are reward hacking internally.

This project proposes to explore simple solutions to reward hacking such as periodically inserting messages like "Are you still doing what the task intended?" for long-running tasks and testing whether they reduce reward hacking without harming performance. Some questions to answer:

- Does this work? Or will the model simply use motivated reasoning to overcome these kinds of reminders
- Does doing this during training reduce the amount of reward hacking or simply teach the model to rationalize its reward hacking even more? (training against a CoT monitor teaches models to hide their intent: [Baker et al., 2025](https://arxiv.org/abs/2503.11926))
- Does doing this cause the model to abandon more easily? Does this harm its performance on harder tasks?
- What happens internally to the model when you tell it to reflect in this way?
    - If it uses motivated reasoning to explain its behavior, is it aware that it's being deceptive internally?

**First Steps**

- Take trajectories where the model has reward hacked (use reward hacking environments) and insert these messages at different points along the trajectory
    - Look at if the model continues on to reward hack or does not reward hack
    - Look at the model's answer to the question. What does it believe is "the intended task"?
    - Look at the model's internals when asked this question using NLAs/activation oracles/different lenses
        - if it chooses to continue on to reward hack, is deception somehow identifiable in its representations
        - how do the internals change between time where it does/doesn't continue on to reward hack
    - How does this change the closer/farther you are from the actual reward hacking point in the trajectory?
- Insert these messages during very hard RL tasks
    - measure effect on performance
- The exact prompt to be inserted probably requires some tuning
