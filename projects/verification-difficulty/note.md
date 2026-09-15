# Measuring AI progress through the difficulty of verification

[AI Evaluation Should Measure Verification Cost, Not Correctness Alone](https://arxiv.org/abs/2608.08709) argues that reliability depends on whether people can detect errors within realistic budgets. It presents this as a conceptual evaluation dimension, leaving room to develop and test concrete measurements.

It would be useful to track AI progress through the human effort and computational resources needed to check its work. Increasingly difficult work and increasingly misleading errors can both raise verification costs, so these effects should be measured separately rather than collapsed into a single capability score.

- Build tasks where correctness can eventually be established independently, including correct outputs and plausible failures.
- Measure human checking time, required expertise, and the cost of programmatic tests or proofs.
- Compare models on matched tasks and compare the difficulty of the hardest work each can reliably complete.
- Test whether explanations, citations, tests, and other supporting evidence reduce checking costs without increasing missed errors.
