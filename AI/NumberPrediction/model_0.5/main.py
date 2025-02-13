import random
import numpy as np

alpha = 0.9 # Learning rate (Higher value means old info will be overwritten more frequantly)
gamma = 0.95 # Discount factor (Higher value means that future reward will be less important)
epsilon = 1.0 # Exploration rate / Randomness factor (Higher value gives a less deterministic result)
epsilon_decay = 0.9995 # Exploration rate decay (The choices will become less random and more deterministic over time)
min_epsilon = 0.01 # The minimum chance for Exploration (At least there will be 1% chance for random action to take place)
episodes = 10000
max_steps = 100

q_table = np.zeros((10,2))

def choose_action(state):
    if random.uniform(0,1) < epsilon:
        return
    else:
        return np.argmax(q_table[state, :])


