---
title: An environment for honesty, calibration, and reporting failures
category: safety
status: Not started
order: 9
---

# An environment for honesty, calibration, and reporting failures

[Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221) studies whether models can estimate answer correctness and recognize their knowledge limits. [Work on monitoring reward hacking](https://arxiv.org/abs/2503.11926) illustrates why successful-looking behavior can still conceal failures of the intended task.

It would be useful to build an environment where a model can succeed, fail, notice uncertainty, and choose what to report. This would let us distinguish inaccurate beliefs from knowingly misleading reports, and test whether training improves both competence and honest communication.

- Give agents tasks with independently logged outcomes, partial information, and occasional tool failures.
- Require predictions of success and explicit reports of completion, uncertainty, and encountered problems.
- Vary the incentives for finishing successfully versus admitting failure, while keeping the true outcome observable to evaluators.
- Train with calibrated rewards and test transfer to unfamiliar failures, auditing whether gains come from better work, better reporting, or superficial compliance.
