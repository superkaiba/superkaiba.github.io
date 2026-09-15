# Predicting reward hacking before it happens

Reward hacking happens when a model gets a high score without doing what the task was actually intended to reward. Catching it after the fact is useful, but ideally we would know before the model takes the action.

[Simple probes can catch sleeper agents](https://www.anthropic.com/research/probes-catch-sleeper-agents) provides an example of using internal activations to detect a hidden behavioral switch. I want to investigate whether related methods can predict reward hacking in agent trajectories, and how early the signal appears.

We would start with a controlled environment where successful task completion and reward hacking can be checked separately. Then we would train probes at different points in the trajectory.

We would check:

- Can we predict a hack before the first problematic action?
- Is the probe detecting intent, an opportunity to hack, or just a recognizable task format?
- Does it transfer to a different environment or a different kind of hack?
- Can the signal support an intervention without repeatedly interrupting legitimate work?
