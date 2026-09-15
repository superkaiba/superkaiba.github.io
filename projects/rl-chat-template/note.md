# Are RL-induced changes concentrated at chat-template positions?

[DeepSeek-R1](https://arxiv.org/html/2501.12948v1) demonstrates that reinforcement learning can substantially change reasoning behavior. Those behavioral results do not tell us where the relevant changes are expressed in a forward pass. One hypothesis is that a large part of the change becomes visible at message boundaries and role-header positions, where a model begins selecting how to respond.

It would be useful to test that hypothesis directly, distinguishing changes at those token positions from changes distributed throughout the response. The role header includes formatting delimiters and ordinary role text; it should not be treated as one universal special “assistant token.”

- Compare matched checkpoints before and after RL on identical tokenized conversations.
- Measure representational changes at role headers, content tokens, reasoning boundaries, and answer tokens.
- Patch activations between checkpoints to test which positions causally affect behavior.
- Repeat across chat templates and RL objectives, controlling for activation magnitude, token frequency, and ordinary prompt-format sensitivity.
