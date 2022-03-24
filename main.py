#### Default Imports ####
import os
import platform
import sys
import time

import config
import savemanager
from player import Player

#### Module Imports ####
from room import Room
from items import Item

# Global Variables
CURRENT_VERSION = "0.0.2"


def get_os_type():
    return platform.system()


def clear():
    """
    Clears the screen
    :return: The current platform
    """
    if get_os_type() == "Windows":
        os.system("cls")
        return "cls"
    elif get_os_type() == "Linux":
        os.system("clear")
        return "clear"
    else:
        return False


def main():  # pragma: no cover
    """
    Main menu

    :return: None
    """
    print("Loading config...")
    settings = config.load()
    clear()
    while True:
        print(
            f"""
        Version: {CURRENT_VERSION}
        ---------------------------------------------

        TextAdventure - by compsup2

        ---------------------------------------------
            """
        )
        choice = prompt("Select an option", "New Game", "Options", "Load a saved game")
        if choice == "1":
            clear()
            rooms = setup_rooms()
            player = Player(input("Name of your character: "), rooms[0])
            gameloop(player, rooms, settings)
        elif choice == "2":
            clear()
            print(
                "These are your current settings, to adjust please edit the"
                " 'config.json' file."
            )
            print(settings)
            input("Press enter to continue...")
        elif choice == "3":
            clear()
            print("Checking for save file...")
            if savemanager.check_for_savefile():
                if (
                    input("Game file found! Do you want to load it? (y/n): ").lower()
                    == "y"
                ):
                    player, rooms = savemanager.load()
                    gameloop(player, rooms, settings, savedgame=True)
                else:
                    print("user aborted loading from file.")
                    input("Press enter to continue...")
            else:
                print("No save file found!")
                input("Press enter to continue...")
        clear()


def setup_rooms():
    """
    Takes the rooms and sets each one of them up so they connect together

    :return: All room classes in a list
    """
    torch = Item(name="Torch", description="A sturdy torch", value=0, lightsource=True)
    blood = Item(
        name="Vial of Blood",
        description="O-negative, this will come in handy.",
        value=50,
    )
    axe = Item(
        name="Death Axe",
        description="Great for killing. Looks like it's been used before!",
        value=75,
    )
    victoryroom = Room(name="endroom", introtext="VICTORY!", is_victory=True)
    thirdroom = Room(
        name="DeathRoom", introtext="All who enter do not leave!", items=[blood, axe]
    )
    secondroom = Room(name="secondroom", introtext="Second Room")
    startroom = Room(
        name="startroom",
        introtext="You get randomly put into a dark. Cave? Well, it looks like one",
        items=[torch],
    )
    rooms = [startroom, secondroom, thirdroom, victoryroom]
    length = len(rooms)
    # Assign next_room to rooms
    for index, room in enumerate(rooms):
        if not index >= length - 1:
            room.next_room = rooms[index + 1]
    # Assign last_room to rooms
    for index, room in enumerate(rooms):
        if not index == 0:
            room.last_room = rooms[index - 1]

    return rooms


# Start of the game
def gameloop(player, rooms, settings, savedgame=False):  # pragma: no cover
    current_room = player.room
    current_room.intro_text()
    
    while player.is_alive() and not player.victory:
        savemanager.save(player, rooms)
        current_room = player.room
        action = choice()
        if action == "inv":
            player.print_inventory()
        elif action == "stat":
            player.print_stats()
        elif action == "debug" and settings["debug_mode"]:
            print(f"Current Room: {current_room.name}")
            print("You are now in debug mode, type 'leave' to exit: ")
            print("Type 'help-debug' for debug commands")
            while True:
                current_room = player.room
                command = choice("DEBUG")
                if command == "room":
                    print(current_room.name)
                elif command == "goto":
                    for room in rooms:
                        print(room.name)
                    answer = input("Go where?: ")
                    for room in rooms:
                        if room.name == answer:
                            player.change_room(room)
                            break
                    else:
                        print("Could not find that room.")
                elif command == "room-info":
                    print(vars(player.room))
                elif command == "leave":
                    print("Leaving DEBUG mode")
                    break
                elif command == "help-debug":
                    valid_commands = ["leave", "room", "goto", "room-info"]
                    for command in valid_commands:
                        print("==> " + command)
        else:
            player.do_action(action)
    if player.victory and player.is_alive():
        with open("endcredits.txt", "r") as f:
            text = f.readlines()
            for line in text:
                print(line)
                time.sleep(1)
            input("Press any key to continue...")
    elif not player.is_alive():
        print("You died! Better luck next time.")
        if choice("Respawn at last checkpoint?"):
            player, rooms = savemanager.load()
            gameloop(player, rooms, settings, savedgame=True)
        else:
            input("Press any key to continue...")


def helpmenu():  # pragma: no cover
    possible_actions = [
        "forward",
        "backward",
        "take",
        "drop",
        "inv",
        "help",
        "stat",
        "search",
    ]
    print("[====== HELP MENU ======]")
    print("Game wide possible actions:\n")
    for action in possible_actions:
        print("=> " + action)
    print("\n[=======================]")


def choice(message: str = None):
    yes = ["yes", "y"]
    while True:
        if message:
            choice = str(input(f"{message} > ")).lower()
        else:
            choice = str(input(f"> ")).lower()

        if choice == "help":
            helpmenu()
        elif choice == "exit":
            if input("Are you sure you want to quit? > ") in yes:
                sys.exit()
        else:
            break

    return choice


def prompt(message: str, *options):
    print(
        f"""

{message}

    """
    )
    i = 0
    for option in options:
        i += 1
        print(f"[{i}] {option}\n\n")
    print("Pick one of the options: ")

    return choice()


if __name__ == "__main__":  # pragma: no cover
    main()
