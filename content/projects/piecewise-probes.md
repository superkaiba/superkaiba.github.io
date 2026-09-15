---
id: "P09"
title: "Piecewise linear and subspace probes"
area: "Representations"
status: "Not started / seed"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Piecewise linear probes"
---

# Piecewise linear and subspace probes

Linear probes are appealing because they are simple and cheap, but they assume that one direction works throughout the representation space. A concept could be easy to decode locally while requiring different directions in different regions.

The [linear representation hypothesis](https://arxiv.org/abs/2311.03658) gives a useful starting point, while [work on concept manifolds](https://arxiv.org/abs/2604.28119) motivates looking beyond a single direction.

I propose to compare ordinary linear probes with piecewise linear probes and subspace probes. A piecewise probe would use different linear rules in different regions; a subspace probe could use several directions together.

We would check:

- Which concepts benefit from these methods?
- Do the different regions correspond to something understandable, such as task, topic, or persona?
- Are improvements still present on new contexts and with matched training data?
- Can we keep most of the simplicity of a linear probe while recovering information that it misses?
