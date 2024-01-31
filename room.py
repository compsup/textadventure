from dataclasses import dataclass, field


@dataclass
class Room:
    name: str
    introtext: str
    last_room: object = None
    next_room: object = None
    is_victory: bool = False
    items: list = field(default_factory=list)
    searched: bool = False

    def intro_text(self):
        """Information to be displayed when the player moves into this room."""
        print(f"\n    {self.introtext}\n")

    def __str__(self):
        return f"{self.name}"
