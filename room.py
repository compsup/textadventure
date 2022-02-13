class Room:
    def __init__(
        self,
        name,
        introtext,
        last_room=None,
        next_room=None,
        is_victory=False,
        items=None,
    ):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.name = name
        self.next_room = next_room
        self.last_room = last_room
        self.introtext = introtext
        self.is_victory = is_victory
        self.searched = False

    def intro_text(self):
        """Information to be displayed when the player moves into this room."""
        print(f"\n    {self.introtext}\n")

    def __str__(self):
        return f"{self.name}"
