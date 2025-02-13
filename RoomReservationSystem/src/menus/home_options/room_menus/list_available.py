from src import Menu

class ListAvailable(Menu):
    def __init__(self):
        self.title = "\nList of Available Rooms\n"
        self.name = "List all available rooms."
        self.children = []
