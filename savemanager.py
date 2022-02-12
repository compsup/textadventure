import os
import pickle

playerFile = "player.pickle"
roomsFile = "rooms.pickle"


def save(player, rooms):
    with open(playerFile, "wb") as f:
        pickle.dump(player, f)
    with open(roomsFile, "wb") as f:
        pickle.dump(rooms, f)


def check_for_savefile():
    return os.path.isfile(playerFile) and os.path.isfile(roomsFile)


def load():
    with open(playerFile, "rb") as f:
        player = pickle.load(f)
    with open(roomsFile, "rb") as f:
        rooms = pickle.load(f)
    return player, rooms
