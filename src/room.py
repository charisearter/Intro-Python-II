# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    def __init__(self, name, description, contents=None, light=False):
        self.name = name
        self.description = description
        self.contents = contents or []
        # if the room is dark /FALSE  if the room has light/TRUE or if have item flashlight.
        self.light = light

    def list_contents(self):
        for items in []:
            print(items.name)