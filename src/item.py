# items class

class Inventory:

    def __init__(self, group, name, description):
        self.name = name
        self.group = group
        self.description = description
        self.items = []

    def __str__(self):
        return f" {self.description}, holds items."


class Items:

    def __init__(self, group, name, description, quest=False):
        self.group = group  # kind of item
        self.name = name
        self.description = description
        self.quest = quest

    def __str__(self):
        return f"{self.name}: {self.description}"


pockets = Inventory('storage', 'Your pockets', 'They aren\'t that deep.')

backpack = Inventory('storage', 'A small backpack',
                     'You can carry a few more items with this.')

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
