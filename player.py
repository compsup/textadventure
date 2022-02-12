class Player:
    def __init__(self, name: str, room):
        self.name = name
        self.health = 100
        self.inv = []
        self.haslightsource = False
        self.victory = False
        self.room = room

    def reduce_health(self, amount: int):
        self.health -= amount
        if self.health <= 0:
            return 0
        else:
            return self.health

    def is_alive(self):
        return self.health > 0

    def print_stats(self):
        print("\n======================")
        print("\nPLAYER STATS:")
        print("\n----------------------")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print("\n======================\n")

    def print_inventory(self):
        print("\n[===== INVENTORY: =====]\n")
        print(f"Number of items: {len(self.inv)}")
        print("          [ITEMS] ")
        for item in self.inv:
            print(item)
        print("\n[======================]\n")

    def do_action(self, action):
        if action == "forward":
            if self.room.next_room:
                self.change_room(self.room.next_room)
                return True
            else:
                print("You smack into a wall, ouch!")
                self.health -= 1
                return False
        elif action == "backward":
            if self.room.last_room:
                self.change_room(self.room.last_room)
                return True
            else:
                print("You smack into a wall, ouch!")
                self.health -= 1
                return False
        elif action == "search":
            if self.room.items:
                print("You look around and find: ")
                for item in self.room.items:
                    print(f"\n=> {item.name}")
                self.room.searched = True
                return True
            else:
                print(self.room.items)
                print("You look around and find nothing but air.")
                return False
        elif action[:4] == "take":
            if self.room.searched:
                for item in self.room.items:
                    if item.name.lower() == action[5:]:
                        self.inv.append(item)
                        print(f"You picked up: {item.name} - {item.description}")
                        self.room.items.remove(item)
                        return True
                    else:
                        print("Cannot find that item")
                        return False
                else:
                    return False
            elif not self.room.searched:
                print("You tried to pick up, air?")
                return False
        else:
            print("NAHH")
            return False

    def change_room(self, new_room):
        self.room = new_room
        self.room.intro_text()
        if self.room.is_victory:
            self.victory = True
