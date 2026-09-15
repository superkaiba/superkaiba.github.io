---
id: "P23"
title: "Storytelling for secret elicitation"
area: "Auditing"
status: "In progress"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Storytelling for secret elicitation"
---

# Storytelling for secret elicitation

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) suggests thinking of the assistant as a character in a story. Separately, work such as [AuditBench](https://arxiv.org/abs/2602.22755) and [password-locked model evaluations](https://arxiv.org/abs/2405.19550) studies how to uncover behaviors or capabilities that a model does not reveal under ordinary questioning.

[Auditing language models for hidden objectives](https://arxiv.org/abs/2503.10965) and [Eliciting Secret Knowledge](https://arxiv.org/abs/2510.01070) already investigate ways to surface concealed information, including persona and continuation-based approaches. They provide baselines for assessing whether storytelling reveals additional information.

We propose to ask the assistant to tell a story about an AI assistant, or a human assistant, with a secret. Does the story reveal something that asking the assistant directly does not, and can we explain the effect through the model's representation of the characters?

We already have preliminary results suggesting that this can work in some settings. The next step is to understand when and why.

Some questions:

- Which kinds of hidden behavior are easiest to elicit this way?
- Does it work differently for behaviors introduced during pretraining versus fine-tuning?
- Can we improve elicitation by intervening on the model's representation of the assistant or story character?
- Can training make a model resistant to this technique?
- What does it tell us about the relationship between the assistant and other personas?

[The Assistant as a Privileged Persona](https://arxiv.org/abs/2606.00545) studies cross-persona self-recognition, giving us a concrete starting point for testing whether the assistant and the story character are represented differently.
