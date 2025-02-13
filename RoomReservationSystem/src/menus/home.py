from src import Menu
from src.menus.home_options import ManageClients, ManageRooms

class Home(Menu):
    def __init__(self):
        self.name = "Home"
        self.children = [ManageClients(), ManageRooms()]
