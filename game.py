class Room:
    """
    Class for representation of different locations.
    """
    def __init__(self, room_type):
        self.room_type = room_type
        self.string = ''
        self.character = None
        self.item = None
        self.path = {}

    def set_description(self, string):
        """
        Assigns a description of the location
        """
        self.string = string

    def link_room(self, other, path):
        """
        Initializes to which location we will move when choosing a part of the world
        """
        self.path[path] = other

    def set_character(self, enemy):
        """
        Set an enemy to this location.
        """
        self.character = enemy

    def set_item(self, item):
        """
        Set an item to this location.
        """
        self.item = item

    def get_details(self):
        """
        Print a description of location.
        """
        print(self.string)

    def get_character(self):
        """
        Return the enemy who is on location.
        """
        return self.character

    def get_item(self):
        """
        Return the item who is on location.
        """
        return self.item

    def move(self,command):
        """
        Move to other location.
        """
        return self.path[command]


class Enemy:
    """
    Class for enemies representation.
    """
    killed = 0

    def __init__(self, name, dis):
        self.name = name
        self.dis = dis
        self.phrase = ''
        self.weakness = ''

    def set_conversation(self, string):
        """
        Assigns a phrase of the location
        """
        self.phrase = string

    def set_weakness(self, string):
        """
        Assigns a weakness of character.
        """
        self.weakness = string

    def describe(self):
        """
        Print a description of enemy.
        """
        print(self.dis)

    def talk(self):
        """
        Print a phrase of enemy.
        """
        print(self.phrase)

    def fight(self, item):
        """
        Return if you win battle or lose.
        """
        if item == self.weakness:
            Enemy.killed += 1
            return True
        else:
            return False

    def get_defeated(self):
        """
        Return a number of enemies which were killed by you.
        """
        return Enemy.killed


class Item:
    """
    Class for item representation on the location.
    """
    def __init__(self, name):
        self.name = name
        self.string = ''

    def set_description(self, string):
        """
        Assigns a description of the location
        """
        self.string = string

    def describe(self):
        """
        Print a description for the item.
        """
        print(self.string)

    def get_name(self):
        """
        Return name of the item.
        """
        return self.name
