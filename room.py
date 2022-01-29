import items


class Room:
    def __init__(self, darkroom: bool = False):
        self.darkroom = darkroom

    def intro_text(self):
        """Information to be displayed when the player moves into this room."""
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()


class StartingRoom(Room):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, player):
        player.inv.append(items.Torch())
