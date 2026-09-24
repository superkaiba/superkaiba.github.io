# Understanding the thinker, talker, and doer personas

**TL;DR:** Investigate whether reasoning, speech, and action involve distinct personas with different goals, and test which influences the others when they disagree.

[The Talker Does Not Control The Doer](https://www.lesswrong.com/posts/cJX2ssssGoYqnijwi/the-talker-does-not-control-the-doer-in-current-ais) argues for distinguishing verbal responses from action selection. [Reasoning Models Generate Societies of Thought](https://arxiv.org/abs/2601.10825) and [Internal Polylogue](https://arxiv.org/abs/2605.09159) motivate also examining the perspectives expressed during reasoning. [Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823) connects persona features with misaligned behavior.

This project compares the thinker, talker, and doer as possible personas or modes of one model. Do they represent the same identity and goals? Does reasoning determine later actions, predict them, or sometimes rationalize a decision already made? These are hypotheses to test, rather than assumptions that each mode is an independent agent.

**First Steps**

- Compare persona features during reasoning, final answers, and tool calls on matched tasks, including which entity is represented as “I.”
- Contrast considering, rejecting, and adopting the same persona under matched wording.
- Prefill or patch one stage with a conflicting persona or goal and measure effects on later reasoning, speech, and actions.
- In trajectories containing a misaligned action, replace the preceding stated intention and test whether the action changes.

**Related project:** [Shared representations across talking, thinking, and acting on values](#values-across-modes) focuses on specific values and transfer between modes.
