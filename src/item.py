# items class

class Inventory:

    def __init__(self, group, name, description, capacity):
        self.name = name
        self.group = group
        self.description = description
        self.capacity = capacity
        self.full = False
        self.items = dict()

    def __str__(self):
        return f" {description}, holds {capacity} items"


class Item:

    def __init__(self, group, name, description):
        self.group = group  # kind of item
        self.name
        self.description

    def __str__(self):
        return f"A {name}: {description}"

# make item objects


brass_knuckles = Item('weapon', 'Brass Knuckles',
                      'A pair of brass knuckles to protect your fingers and give your punches extra power.')

hp_potion = Item('healing', 'Health Potion',
                 'A vial of red liquid that is said to heal your HP completely.')

mp_potion = Item('healing', 'Magic Potion',
                 'A vial of blue liquid that is said to heal your MP completely')

antidote = Item('healing', 'Antidote',
                'Cures you of poison. Does nothing for your HP though.')

book = Item('skill', 'Old book',
            'An old worn book. Looks to be a sort of manuel of some kind.')

sm_backpack = Item('storage', 'A small backpack', 'You can carry a couple more items with this.')
