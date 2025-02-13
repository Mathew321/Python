import os

class Menu:
    def __init__(self) -> None:
        self.name: str = ""
        self.children: list[Menu] = []

    def fetchOptions(self) -> None:
        for i in range(0,len(self.children)):
            print("       " + str(i+1) + "." + self.children[i].name)
        print("       0. Exit\n")

    def clear(self):
        os.system("clear")

    def stepInto(self, title=None) -> None:
        while True:
            if title != None:
                print(title)

            self.fetchOptions()
        
            try:
                option: int = int(input("Option: ")) -1
            except ValueError:
                option = -69

            self.clear()

            if option > -1 and option <= len(self.children) - 1:
                child: Menu = self.children[option]
                child.stepInto(child.title)
            elif option == -1:
                break
            else:
                print("Invalid option, try again!\n")
