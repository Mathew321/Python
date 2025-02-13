import os, random, sys, time
from collections import Counter

class DiceGame:
    def __init__(self):
        self.clear = self.get_clear_command()
        self.dice = [0, 0, 0, 0, 0, 0]
        self.picked = []
        self.score = 0

    def get_clear_command(self):
        return lambda: os.system("cls" if os.name == "nt" else "clear") if sys.stdout.isatty() else lambda: None

    def roll(self):
        self.dice = [random.randint(1, 6) for _ in range(len(self.dice))]

    def choose(self):
        try:
            choice = input("Which dice would you like to pick?\nChoose up to 3 indexes (1-6): ")
            indexes = [int(i) - 1 for i in choice if i.isdigit()]
            if 1 <= len(indexes) <= 3 and all(0 <= i < len(self.dice) for i in indexes):
                return sorted(set(indexes), reverse=True)
            else:
                print("Invalid indexes. Try again.\n")
                return self.choose()
        except (ValueError, EOFError):
            print("Invalid input. Try again.\n")
            return self.choose()

    def pick(self, picks):
        picks.sort(reverse=True)
        for p in picks:
            self.picked.append(self.dice[p])
        for p in picks:
            self.dice[p] = -1
        self.dice = [die for die in self.dice if die != -1]

    def evaluate(self):
        counts = Counter(self.picked)
        score = 0
        triplets = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
        straights = {
            (1, 2, 3, 4, 5, 6): 1500,
            (1, 2, 3, 4, 5): 750,
            (2, 3, 4, 5, 6): 750,
            (3, 4, 5, 6): 500,
            (1, 2, 3, 4): 500,
            (2, 3, 4, 5): 500
        }

        for straight, value in straights.items():
            if all(counts[n] >= 1 for n in straight):
                score += value
                for n in straight:
                    counts[n] -= 1

        for num in list(counts.keys()):
            if counts[num] >= 3:
                multiplier = 1 + (counts[num] - 3)
                score += triplets[num] * multiplier
                counts[num] -= counts[num]

        score += counts[1] * 100
        score += counts[5] * 50
        counts[1] = 0
        counts[5] = 0

        if any(counts.values()):
            return 0

        return score if score > 0 else 0

    def start(self):
        running = True
        length = len(self.dice)

        arrow_title = "            "
        index_title = "Indexes:    "
        index_strings = {6: "  1  2  3  4  5  6", 5: "  1  2  3  4  5", 4: "  1  2  3  4", 3: "  1  2  3", 2: "  1  2", 1: "  1"}

        total_index_string = arrow_title + "  |" * length + "\n" + index_title + index_strings[length]

        roll_title = "Rolling dice..."

        while running:
            self.clear()
            if self.picked:
                print("Picked dice: ", str(self.picked).strip("[]"))

            if len(self.picked) == 6:
                break

            roll_decision = input("Do you want to roll? (y/n): ").lower()
            if roll_decision != 'y':
                break
            else:
                print(roll_title)
                time.sleep(1.0)

            self.roll()

            print("\nRolled dice: ", str(self.dice).strip("[]"))
            print(total_index_string)

            choice = self.choose()

            self.pick(choice)

            total_index_string = arrow_title + "  |" * len(self.dice) + "\n" + index_title + index_strings[len(self.dice)]

        self.score = self.evaluate()
        self.stop()

    def stop(self):
        print("Your score: ", self.score)

    def replay(self):
        pass

def main():
    try:
        DiceGame().start()
    except Exception as e:
        print(f"[INFO] {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[INFO] {e}")

