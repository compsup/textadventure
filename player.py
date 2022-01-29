import items


class Player:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.inv = []
        self.haslightsource = False
        self.victory = False

    def reduce_health(self, amount: int):
        self.health = - amount
        if self.health <= 0:
            return False
        else:
            return self.health

    def is_alive(self):
        return self.health > 0

    def stats(self):
        print("\n======================")
        print("\nPLAYER STATS:")
        print("\n----------------------")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print("\n======================\n")

    def inventory(self):
        print("\n======================")
        print("\nINVENTORY:")
        print(f"Number of items: {len(self.inv)}")
        print("       -| ITEMS |-")
        for item in self.inv:
            print(item)
        print("\n======================\n")
