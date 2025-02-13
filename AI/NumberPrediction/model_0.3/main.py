import random

first = 0
last = 100

while True:
    guess = random.randint(first,last)
    print(f"Guess: {guess}")
    user_input = input("Enter higher/lower/correct (or 'q' to quit): ").lower()
    if user_input == 'q':
        print("Exiting...")
        break
    elif user_input == "higher":
        first = guess if guess == 100 else guess + 1
    elif user_input == "lower":
        last = guess if guess == 0 else guess - 1
    elif user_input == "correct":
        print("Yay!")
        break
    else:
        print("\nInvalid input.\nTry again!\n")
