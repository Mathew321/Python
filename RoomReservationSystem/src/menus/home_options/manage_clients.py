from src import Menu
from src.menus.home_options.client_menus.add_client import AddClient
from src.menus.home_options.client_menus.search_client import SearchClient

class ManageClients(Menu):
    def __init__(self):
        self.title = "\nClient Manage Menu\n"
        self.name = "Manage clients"
        self.children = [AddClient(), SearchClient()]
