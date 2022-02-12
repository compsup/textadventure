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
            return False
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
        else:
            return False

    def change_room(self, new_room):
        self.room = new_room
        self.room.intro_text()
        if self.room.is_victory:
            self.victory = True
