# Write a class
# to hold player information, e.g. what room they are in
# currently.

# add backpack for player to hold items
# backpack should have item limit
class Player:

    def __init__(self, location, inventory=None):

        self.location = location
        self.inventory = []

    def insert(self, item):
        self.inventory.items.append(item)

    def check_inventory(self):
        if len(self.inventory.items) > 0:
            for items in self.inventory.items:
                print(items.name)
        else:
            print('You have nothing.')

    def has_light(self, item, location):
        for item in self.inventory.items:
            if item.name == 'Flashlight':
                print('You can use your flashlight in dark areas')
            else:
                self.location = self.location
                print('You can\'t see. The room is too dark. You need a light source.')

    def pickup(self, item):
        self.inventory.items.append(item)
        self.location.contents.remove(item)
        print('Looted everything like you should in an adventure game.')

    def drop(self):
        ans = input('What do you want to drop?: ')
        for items in self.inventory.items:
            if ans.lower().strip() == items.name.lower().strip():
                self.inventory.items.remove(items)
