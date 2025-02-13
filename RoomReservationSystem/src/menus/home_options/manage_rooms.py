from src import Menu
from src.menus.home_options.room_menus.list_available import ListAvailable
from src.menus.home_options.room_menus.list_occupied import ListOccupied
from src.menus.home_options.room_menus.list_ooo_rooms import ListOooRooms

class ManageRooms(Menu):
    def __init__(self):
        self.title = "\nRoom Manage Menu\n"
        self.name = "Manage rooms"
        self.children = [ListAvailable(), ListOccupied(), ListOooRooms()]
