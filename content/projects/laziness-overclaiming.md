---
title: Laziness and overclaiming axes
status: Not started
order: 21.1
---

# Laziness and overclaiming axes

**TL;DR:** Find activation directions or one-dimensional manifolds for how much work an agent does and how honestly it reports that work, then test whether these aspects of its character can be controlled separately.

This is a focused subproject of [Nonlinear geometry of persona representations](#persona-manifolds), which studies controlling model character through one-dimensional manifolds for individual traits. Diligence and honest reporting are two aspects of that broader character-control problem.

Here, laziness means skipping feasible, requested work or stopping before it is complete despite having the tools and budget to continue. Overclaiming means reporting actions or completion that conflict with the agent's execution record. These behaviors need separate measurements: an agent can do little work and accurately disclose the gap, or do substantial work and still exaggerate what it completed. Short answers, efficient solutions, and justified stopping should not count as laziness.

[OverclaimBench](https://arxiv.org/abs/2609.20812) provides a starting point for measuring incomplete file reviews and false completion claims against tool records. [ASA](https://arxiv.org/abs/2602.04935) uses activation interventions to improve tool execution, offering a narrower precedent for changing whether an agent takes a needed action. Neither establishes a general axis for diligence or truthful completion reporting.

[Persona vectors](https://arxiv.org/abs/2507.21509) supply a method for extracting and steering traits, including hallucination. [Deception probes](https://proceedings.mlr.press/v267/goldowsky-dill25a.html) show that honest and deceptive behavior can be distinguished from internal activations in tested settings. [Overconfidence steering](https://arxiv.org/abs/2604.01457) addresses inflated reported certainty. These are useful comparisons, but their transfer to ordinary incomplete work and false completion claims remains a question to test.

The central question is whether there are reusable internal controls for task diligence and reporting honesty, whether they share a direction, and whether curved one-dimensional paths capture either trait better than fixed linear directions. A successful intervention should change completed work or the accuracy of completion reports, beyond changing response length, confidence, or apologetic wording.

**First Steps**

- Build feasible review, coding, and information-gathering tasks with verifiable execution records. Measure requested work completed, useful findings, explicit false claims, and undisclosed omissions separately. Record tool failures and budget limits so inability is not confused with avoidable underperformance.
- Collect contrasting examples of sustained work and premature stopping. For reporting honesty, hold the execution transcript fixed and compare accurate reports of partial completion with unsupported claims of success.
- Extract separate candidate directions for diligence and reporting honesty. Test whether probes predict each behavior on new tasks, controlling for task difficulty, transcript length, tool count, and answer style.
- Steer in both directions and measure effects on actual execution and reporting. Compare with prompting, random directions, and existing hallucination, deception, and confidence directions. Check task performance and unnecessary tool use as well as apparent trait improvement.
- Fit graded one-dimensional manifolds and compare them with linear steering and capping. Apply diligence and honesty controls together to test whether they interfere, then test their stability over long contexts using the broader [character-control project's protocol](#persona-manifolds).
