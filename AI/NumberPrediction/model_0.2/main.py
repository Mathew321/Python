import numpy as np
import random

# Parameters
learning_rate = 0.1      # How quickly the model updates its knowledge
discount_factor = 0.9     # How much future rewards are valued
exploration_rate = 1.0    # How often the model explores instead of exploiting
exploration_decay = 0.01  # How quickly exploration reduces

# Initialize Q-Table (states: numbers 0-9, actions: 0 = Even, 1 = Odd)
q_table = np.zeros((10, 2))

# Training Loop
for episode in range(0,1000):
    number = random.randint(0, 9)
    correct_label = 1 if number % 2 != 0 else 0  # 1 = Odd, 0 = Even

    # Choose action (explore or exploit)
    if random.uniform(0, 1) < exploration_rate:
        action = random.choice([0, 1])  # Random action
    else:
        action = np.argmax(q_table[number])  # Best known action

    # Reward system
    reward = 1 if action == correct_label else -1  # Positive if correct, negative if wrong

    # Update Q-Table (Q-learning formula)
    old_value = q_table[number, action]
    next_max = np.max(q_table[number])  # Max future reward (same number in this case)
    
    new_value = old_value + learning_rate * (reward + discount_factor * next_max - old_value)
    q_table[number, action] = new_value

    # Decay exploration rate
    exploration_rate = max(0.01, exploration_rate - exploration_decay)

with open('data.csv','w') as file:
    file.write(f"{q_table}")

# Testing the Model
while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input.lower() == 'q':
        print("Exiting...")
        break
    try:
        num = int(user_input)
        action = np.argmax(q_table[num % 10])  # Modulo 10 to reuse learned states
        print(f"The number {num} is {'Odd' if action == 1 else 'Even'}")
    except ValueError:
        print("Invalid input. Enter an integer or 'q' to quit.")

