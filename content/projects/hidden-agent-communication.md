---
title: What do agents communicate beyond the apparent meaning of their messages?
status: Not started
order: 63
---

# What do agents communicate beyond the apparent meaning of their messages?

[Subliminal Learning](https://arxiv.org/abs/2507.14805) shows that training on another model's outputs can transfer traits through text without explicitly discussing them. [Hidden in Plain Text](https://arxiv.org/abs/2410.03768) separately studies elicited steganographic communication between language models. Neither result by itself establishes how much hidden information agents exchange during an ordinary live conversation.

It seems important to test whether one agent can infer another's internal state from messages in ways that a human reader or monitor misses, and whether this helps explain swarm behavior.

- Give a sender controlled private states and test what a receiver can recover from its task-relevant messages.
- Compare receiver predictions with human or model monitors and direct activation readouts.
- Paraphrase messages, control formatting and remove shared context to identify which signals carry information.
- Distinguish spontaneous inference, deliberately trained covert communication and weight updates from passive exposure; test their effects on coordination and correlated failures.
