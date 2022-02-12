class Room:
    def __init__(self, actions, name, introtext, last_room=None, next_room=None, is_victory=False):
        self.roomlooted = False
        self.actions = actions
        self.name = name
        self.next_room = next_room
        self.last_room = last_room
        self.introtext = introtext
        self.is_victory = is_victory

    def intro_text(self):
        """Information to be displayed when the player moves into this room."""
        print(f'\n    {self.introtext}\n')

    def __str__(self):
        return f"{self.name}"
