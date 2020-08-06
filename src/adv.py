# from file name import Class
from room import Room
from player import Player
# import all from file
import item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons...", [item.backpack]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item.book]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item.mp_potion, item.brass_knuckles]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item.hp_potion]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all items


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
#

# Add Items to room

# Main
#
directions = ['n', 's', 'e', 'w', 'q',
              'north', 'south', 'east', 'west', 'quit']
# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'], inventory=[])
player.inventory = item.pockets
# Write a loop that:
#
while True:
    # * Prints the current room name
    location = player.location
    print('\n ****************************** \n')
    print('\n game info blurb here \n')
    print('\n ****************************** \n')
    print(
        f'You are in the {location.name}. {location.description}\n There are {len(location.contents)} item(s) in the room.\n')
    print(f'{player.inventory} to hold anything you find.\n')
    print('Where do you want to go? What do you want to do? \n')
    cmd = input('Pick an action or direction: ')
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

    if cmd.lower() in ('q', 'quit'):
        break
    elif cmd.lower() in ('n', 'north'):
        if hasattr(location, 'n_to'):  # hasattr lookes to see if something has the attribute
            print('You chose North')
            player.location = location.n_to
        else:
            print('An invisible barrier blocks your path. Choose another direction.')
    elif cmd.lower() in ('s', 'south'):
        if hasattr(location, 's_to'):
            print('You chose South')
            player.location = location.s_to
        else:
            print('An invisible barrier blocks your path. Choose another direction.')
    elif cmd.lower() in ('e', 'east'):
        if hasattr(location, 'e_to'):
            print('You chose East')
            player.location = location.e_to
        else:
            print('An invisible barrier blocks your path. Choose another direction.')
    elif cmd.lower() in ('w', 'west'):
        if hasattr(location, 'w_to'):
            print('You chose West')
            player.location = location.w_to
        else:
            print('An invisible barrier blocks your path. Choose another direction.')
