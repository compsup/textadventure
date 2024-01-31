from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    room: object
    inv: list = field(default_factory=list)
    health: int = 100
    haslightsource: bool = False
    victory: bool = False
    if inv is None:
        inv = []

    def reduce_health(self, amount: int):
        self.health -= amount
        if self.health <= 0:
            return 0
        else:
            return self.health

    def is_alive(self):
        return self.health > 0

    def print_stats(self):  # pragma: no cover
        print("\n======================")
        print("\nPLAYER STATS:")
        print("\n----------------------")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print("\n======================\n")

    def print_inventory(self):  # pragma: no cover
        print("\n[===== INVENTORY: =====]\n")
        print(f"Number of items: {len(self.inv)}")
        print("          [ITEMS] ")
        for item in self.inv:
            print(item)
        print("\n[======================]\n")

    def forward(self):
        if self.room.next_room:
            self.change_room(self.room.next_room)
            return True
        else:
            print("You smack into a wall, ouch!")
            self.health -= 1
            return False

    def backward(self):
        if self.room.last_room:
            self.change_room(self.room.last_room)
            return True
        else:
            print("You smack into a wall, ouch!")
            self.health -= 1
            return False

    def search(self):
        if self.room.items:
            print("You look around and find: ")
            for item in self.room.items:
                print(f"\n=> {item.name}")
            self.room.searched = True
            return True
        else:
            print("You look around and find nothing but air.")
            return False

    def take_item(self, item_name):
        if self.room.searched:
            for item in self.room.items:
                if item.name.lower() == item_name:
                    self.inv.append(item)
                    print(f"You picked up: {item.name} - {item.description}")
                    self.room.items.remove(item)
                    return True
            else:
                print("Cannot find that item")
                return False
        elif not self.room.searched:
            print("You tried to pick up, air?")
            return False

    def drop_item(self, item_name):
        for item in self.inv:
            if item.name.lower() == item_name:
                self.room.items.append(item)
                self.inv.remove(item)
                print(f"You dropped: {item.name}")
                return True
        else:
            print("You don't have that item in your inventory!")
            return False

    def do_action(self, action):
        if action == "forward":
            return self.forward()
        elif action == "backward":
            return self.backward()
        elif action == "search":
            return self.search()
        elif action[:4] == "take":
            return self.take_item(action[5:])
        elif action[:4] == "drop":
            return self.drop_item(action[5:])

        else:
            print("NAHH")
            return False

    def change_room(self, new_room):
        self.room = new_room
        self.room.intro_text()
        if self.room.is_victory:
            self.victory = True
