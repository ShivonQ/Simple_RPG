#same thing, don't see the need to inherit from other classes (maybe Item?)


class Inventory():
    def __init__(self, owner):
        self.inventory = {}
        self.owner = owner
    def add_item(self, item):
        self.inventory[item.name] = item

#    TODO: A method to print the inventory