from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Training Data
X = np.array([[i] for i in range(10)])  # Numbers 0-9
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])  # 0 = Even, 1 = Odd

# Model
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X, y)

# Check Predictions on Training Data
for num in range(10):
    prediction = model.predict([[num]])[0]
    print(f"Prediction for {num}: {'Odd' if prediction == 1 else 'Even'}")

# User Input Loop
while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input.lower() == 'q':
        print("Exiting...")
        break
    try:
        num = int(user_input)
        prediction = model.predict([[num]])
        print(f"The number {num} is {'Odd' if prediction[0] == 1 else 'Even'}")
    except ValueError:
        print("Invalid input. Enter an integer or 'q' to quit.")

