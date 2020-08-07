# items class

class Inventory:

    def __init__(self, group, name, description, capacity):
        self.name = name
        self.group = group
        self.description = description
        self.capacity = capacity
        self.full = False  # set to true if capacity is maxed out
        self.items = dict()

    def __str__(self):
        return f" {self.description}, holds {self.capacity} items"

    ''' check if inventory is full depending on item '''


class Items:

    def __init__(self, group, name, description, quest=False):
        self.group = group  # kind of item
        self.name = name
        self.description = description
        self.quest = quest

    def __str__(self):
        return f"{self.name}: {self.description}"


class Quest(Items):
    def __init__(self, group, name, description, quest, sell=False):
        self.sell = sell
        super().__init__(group, name, description, quest=True)

    def __str__(self):
        return " {0.name}: {0.description}".format(self)


pockets = Inventory('storage', 'Your pockets', 'They aren\'t that deep.', 2)

backpack = Inventory('storage', 'A small backpack',
                     'You can carry a few more items with this.', 7)

brass_knuckles = Items('weapon', 'Brass Knuckles',
                       'A pair of brass knuckles to protect your fingers and give your punches extra power.')

hp_potion = Items('healing', 'Health Potion',
                  'A vial of red liquid that is said to heal your HP completely.')

mp_potion = Items('healing', 'Magic Potion',
                  'A vial of blue liquid that is said to heal your MP completely')

antidote = Items('healing', 'Antidote',
                 'Cures you of poison. Does nothing for your HP though.')

book = Items('skill', 'Old book',
             'An old worn book. Looks to be a sort of manuel of some kind.')

flashlight = Items('key_item', 'Flashlight',
                   'A flashlight to help you see in dark places.', True)

escape = Items('exit', 'Escape',
               'If used, teleports the person outside to a safe location.')
