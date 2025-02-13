# Building my own ai

This is a fun little project where I explore RL/ML (Reinforcement Learning / Machine Learning). The purpose of RL is
to make a system that would be able to determine correct action vs incorrect ones. This could lead to a system learning
to complete tasks based on the decision it makes. Because you we favor one decision over the other the AI would start to
make the correct decision almost always.

## Q-Learning

Q-Learning is the process of learning to make a complete AI model from scratch. This model will not understand the
environment it's in because it's purpose is to only make correct decisions like I explained earlier not to understand
what it's actually doing.

### Core concepts of Q-Learning

1. State: the current situation
2. Action: What the model decides to do
3. Reward: You define this! Positive for correct answers, negative for wrong ones.
4. Q-Table: A table where the model stores what it's learned--mapping states to actions.

## Model_0.1

This was a simple test of making an AI that would recognise the pattern for odd or even numbers.

## Model_0.2

This model is a very succesfull model that will decide whether a number is odd or even based on the trained data.

## Model_0.3

This isn't an RL, but a rule based model which is simpler.
