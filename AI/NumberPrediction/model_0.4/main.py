import os, random, json, numpy as np

class AI:
    def __init__(self):
        # Load or initialize the Q-table
        self.q_table = np.zeros((, ))
        self.alpha = 0.1  # Learning rate
        self.gamma = 0.9  # Discount factor
        self.epsilon = 0.1  # Exploration rate
        self.epsilon_decay = 0.9995 # Exploration decay
    
    

class Game:
    def __init__(self):
        self.clear = lambda: os.system("clear")
        self.board = [[" ", " ", " ", "1"],
                      [" ", " ", " ", "2"],
                      [" ", " ", " ", "3"]]
        self.ai = AI()

        self.win = False
        self.draw = False
        self.winner = ""

    def print_board(self):
        print("   1  2  3")
        for row in self.board:
            print(row[3], row[0], "|", row[1], "|", row[2])
            if row != self.board[-1]:
                print("  ---------")
        print()

    def check_winner(self, o):
        if o == "X":
            self.winner = "Player"
        elif o == "O":
            self.winner = "AI"

    def evaluate(self, o):
        # Check rows
        for row in self.board:
            if row[:-1] == [o, o, o]:
                self.win = True
                self.check_winner(o)

        # Check columns
        for i in range(3):
            if self.board[0][i] == o and self.board[1][i] == o and self.board[2][i] == o:
                self.win = True
                self.check_winner(o)

        # Check diagonals
        if self.board[1][1] == o:
            if (self.board[0][0] == o and self.board[2][2] == o) or (self.board[0][2] == o and self.board[2][0] == o):
                self.win = True
                self.check_winner(o)

        # Check for draw
        if not self.win and all(cell != " " for row in self.board for cell in row[:-1]):
            self.draw = True

    def move(self, o):
        try:
            if o == "X":
                m = input("Give index of the row and column (e.g., 12 for row 1, col 2 or 'q' to quit): ")
            elif o == "O":
                m = self.ai.move(self.board)

            if m.lower() == 'q':
                print("Game exited.")
                exit()

            if len(m) != 2 or not all(d.isdigit() for d in m):
                print("\nInvalid input.\nTry again!\n")
                self.move(o)
                return

            row, col = int(m[0]) - 1, int(m[1]) - 1
            if not (0 <= row < 3 and 0 <= col < 3):
                print("\nOut of bounds!\nTry again!\n")
                self.move(o)
                return

            if self.board[row][col] != " ":
                print("\nCell already taken.\nTry again!\n")
                self.move(o)
                return

            self.board[row][col] = o
            self.evaluate(o)
        except ValueError:
            print("\nInvalid input.\nTry again!\n")
            self.move(o)

    def start(self):
        XO = ["X", "O"]

        for i in range(9):  # Max 9 moves in Tic-Tac-Toe
            self.clear()
            self.print_board()
            self.move(XO[i % 2])

            if self.win:
                self.clear()
                self.print_board()
                print(f"The {self.winner} won!")
                break
            if self.draw:
                self.clear()
                self.print_board()
                print("The game ended in a draw!")
                break

def test():
    ai = AI()
    board = [["X", "O", " "], 
             [" ", "X", " "], 
             [" ", " ", "O"]]
    # move = ai.train(board)
    # print(type(move))

def main():
    Game().start()
    # test()
    
if __name__ == "__main__":
    main()
