---
id: "P04"
title: "First-person and third-person identity in prompts"
area: "Personas"
status: "Not started / seed"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "How does the model represent first person vs third person (in the system prompt + internal)"
---

# First-person and third-person identity in prompts

When we give a model a role, we can say “you are a programmer,” “the assistant is a programmer,” or “AIs are programmers.” These sound similar, but they do not quite refer to the same thing.

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) motivates asking how a role becomes associated with the assistant. Work on [the assistant as a privileged persona](https://arxiv.org/abs/2606.00545) is also relevant to how models distinguish themselves from other characters.

[How do Language Models Bind Entities in Context?](https://arxiv.org/abs/2310.17191) studies how models attach attributes to the right entity. That gives us a mechanistic starting point for asking whether a trait is bound to the assistant, the user, or a third-person character.

I propose to compare first-person, second-person, and third-person descriptions while keeping the role and task fixed. We would look at both what the model does and how it represents the identity being described.

Some questions:

- Do “I,” “you,” “the assistant,” and “an AI” activate the same role representation?
- Does it matter whether the description appears in the system prompt or a user message?
- Which formulations most strongly change the assistant's behavior?
- Can we transfer a trait from a third-person character to the assistant by intervening on the relevant activations?
