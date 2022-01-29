class Item:
    def __init__(self, name: str, description: str, value, durability: int = 100, lightsource: bool = False):
        self.name = name
        # If the item gives off light (like a torch)
        self.lightsource = lightsource
        self.durability = durability
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Torch(Item):
    def __init__(self):
        super().__init__(name="Torch",
                         description="A sturdy torch, suitable for lighting up dark places.", value=0, durability=10)
