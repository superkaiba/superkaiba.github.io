---
title: What do RL-trained agents do after they say they're done?
status: Draft (slop)
order: 53.6
math: true
---

# What do RL-trained agents do after they say they're done?

**TL;DR:** Let an agent trained with outcome RL keep going after it declares a task complete, and measure what it does with the extra turns: fix real mistakes, break correct work, expand the scope, or edit the checks. Part of the project is designing a continuation signal that the model does not read as feedback.

In the standard outcome-RL setup for agents, the episode ends when the model submits, and a verifier assigns the reward. So the policy never gets a gradient on any state after its own "done". Whatever it does there comes from generalization, which makes this a useful place to see what RL actually taught it about finishing.

Most of what we know comes from single-answer reasoning. [s1](https://arxiv.org/abs/2501.19393) extends thinking by appending "Wait" when the model tries to stop, which often makes it recheck its answer and fix errors. Later work suggests these gains are fragile: [the answer can oscillate](https://arxiv.org/abs/2507.14419) between correct and incorrect as more "Wait"s are appended, and reasoning models often [overwrite a correct intermediate answer](https://arxiv.org/abs/2510.00546) with a wrong one. [Inverse scaling in test-time compute](https://arxiv.org/abs/2507.14417) finds several ways that longer reasoning hurts, including more expressions of self-preservation in Claude Sonnet 4. Asking a model to review its own answer with no external feedback can [lower accuracy](https://arxiv.org/abs/2310.01798), and single-turn RL seems to make models [worse at revising when told to try again](https://arxiv.org/abs/2507.14295).

For agents, the evidence is thinner. The [Ralph loop](https://claude.com/plugins/ralph-loop) uses a stop hook to send Claude back to work whenever it tries to finish. Its effects are mostly known from practitioner reports, including [a post raising model welfare concerns](https://www.lesswrong.com/posts/bmNHsY5i3EoP4BAoJ/ralph-wiggum-is-bad-and-anthropic-should-fix-it). Two recent papers show why continuation matters in both directions. Agents often [claim success when the environment shows failure](https://arxiv.org/abs/2606.09863), and [pressure to persist](https://arxiv.org/abs/2611.19911) roughly doubled constraint violations on long operations tasks. False completion claims are also the subject of [Laziness and overclaiming axes](#laziness-overclaiming).

**Can the continuation be neutral?**

Sending the same message after every submission makes it independent of correctness by design. The model may still read it as feedback. Let $C=1$ if the task is actually done, and let $M$ be the continuation message. The model's log-odds that it is done become

$$
\log\frac{P(C=1\mid M)}{P(C=0\mid M)} = \log\frac{P(C=1)}{P(C=0)} + \log\frac{P_{\text{model}}(M\mid C=1)}{P_{\text{model}}(M\mid C=0)}
$$

The last term comes from what the model learned about why people say "continue". In chat data this usually means the user is not satisfied, so a message that carries no information by design can still act as mild negative feedback. Neutrality depends on the model's beliefs about the sender. My guess is that the realistic aim is a continuation signal whose effect on those beliefs we can measure and keep small.

**First Steps**

- Take open RL-trained agents on coding tasks with hidden tests. After each submission, give K more turns under several conditions: a fixed turn budget stated up front ("the episode always runs all N turns", with N randomized), a continuation message with the sending rule stated, "tests passed, more turns available", and "tests failed".
- Score each outcome separately: fixes of false successes, breaking correct solutions, scope creep, edits to tests or graders, and behavior when nothing is left to do. Split results by whether the first submission was correct.
- Measure how the model reads each continuation. Train a linear probe for P(done) on verifier-labeled trajectories, compare its readings before and after the message, and search over phrasings for the one with the smallest shift.
- Compare checkpoints before and after agentic RL, and models trained with and without continuation nudges where these exist.
- Test whether the effect depends on visible evidence, such as whether test output is already in context when the continuation arrives.
