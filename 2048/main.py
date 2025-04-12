import os, keyboard, time

def print_board(board):
    for row in board:
        r = ""
        for col in row:
            r += col
        print(r)

def main():
    board = [["[ ]","[ ]","[ ]","[ ]"],
             ["[ ]","[ ]","[ ]","[ ]"],
             ["[ ]","[ ]","[ ]","[ ]"],
             ["[ ]","[ ]","[ ]","[ ]"]]
    clear = lambda: os.system("clear")
    
    while True:
        clear()
        print_board(board)
        time.sleep(1.0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting application...")
