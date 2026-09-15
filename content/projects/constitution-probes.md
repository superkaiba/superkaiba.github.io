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

A model's constitution can contain many different principles: be honest, follow the user's intent, avoid harmful actions, and so on. It would be useful to detect violations with one internal monitor, instead of building a separate detector for every possible failure.

[Constitutional Classifiers](https://www.anthropic.com/news/constitutional-classifiers) and [work on reusing a model's representations for monitoring](https://alignment.anthropic.com/2025/cheap-monitors/) provide starting points. The question here is how far we can extend that approach across a broader set of principles.

I propose to start with a small constitution and examples that distinguish its different rules. We could compare a shared probe against separate probes for each rule, then gradually expand the constitution.

Some questions:

- Is there a shared representation of “this violates the instructions/principles,” or does each rule need its own direction?
- Can a probe trained on some violations recognize new kinds of violations?
- Can it distinguish an actual violation from a harmless discussion of one?
- How does performance change when the constitution itself changes?
