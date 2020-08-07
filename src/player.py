# Write a class
# to hold player information, e.g. what room they are in
# currently.

# add backpack for player to hold items
# backpack should have item limit
class Player:

    def __init__(self, location, inventory=None):

        self.location = location
        self.inventory = inventory or []

    def has_item(self):
        pass

    def pickup(self, item):
        pass

    def drop(self, item):
        pass
