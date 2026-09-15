---
id: "P02"
title: "Probing for violations of a whole constitution"
area: "Monitoring"
status: "Not started / seed"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Can you probe for an entire constitution violation?"
---

# Probing for violations of a whole constitution

A model's constitution can contain many different principles: be honest, follow the user's intent, respect privacy, avoid harmful actions, and so on. I want to know whether we can train **one activation probe to detect a violation of any part of the entire constitution**, including kinds of violations that were absent from the probe's training data.

[Constitutional Classifiers](https://www.anthropic.com/news/constitutional-classifiers) turns written policies into training data for safety classifiers, and [Cost-Effective Constitutional Classifiers](https://alignment.anthropic.com/2025/cheap-monitors/) reuses a model's internal representations for monitoring. These provide practical starting points for building the probe.

The closest internal-monitoring work, [Constitutional Value Potentials](https://arxiv.org/abs/2606.15420), studies priority conflicts among six predefined values. It learns value-specific directions and combines their pairwise margins into an “any violation” score over the active clauses. It also tests held-out conflicts among those values. This is useful evidence for structured monitoring, but it does not establish a single probe that covers a full, broad natural-language constitution or a shared representation that generalizes to entirely new kinds of principles.

I propose to start with a small constitution, compare a shared probe against separate rule probes and the value-margin approach, and then expand toward a full constitution. The shared probe would have to identify violations without being told which rule is relevant for each example.

We would check:

- Is there a shared representation of “this violates the constitution,” or do different rules require different directions?
- Can training on some rule families transfer to held-out families, beyond new examples of familiar violations?
- Does coverage degrade as we add more varied principles to the constitution?
- Can the probe distinguish a violation from a harmless discussion, quotation, or permitted exception?
- When we change the constitution, does the probe track the new rules rather than the model's usual preferences?
