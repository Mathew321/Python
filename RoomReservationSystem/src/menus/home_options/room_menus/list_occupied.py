from src import Menu

class ListOccupied(Menu):
    def __init__(self):
        self.title = "\nList of Occupied Rooms\n"
        self.name = "List all occupied rooms."
        self.children = []
