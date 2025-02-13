# Imports
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Game Of Life")
        self.geometry("1280x720")
        self.configure(background="#1B2838")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=1)

# Main Loop
def main():
  # Initialize app
  app = Window()
  app.mainloop()

# Initialize Main Loop run
if __name__ == "__main__":
  main()
