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

# Global Variables
CURRENT_VERSION = "0.0.1"


def clear():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')
    else:
        print(f'Your OS: {platform.system()}, is not currently supported!')
        input("Press enter to exit...")
        sys.exit()
    return platform.system()


def main():
    print("Loading config...")
    settings = config.load()
    clear()
    while True:
        print(f'''
        Version: {CURRENT_VERSION}
        ---------------------------------------------

        TextAdventure - by compsup2

        ---------------------------------------------
            ''')
        choice = prompt("Select an option", "New Game", "Options", "Load a saved game")
        if choice == "1":
            clear()
            rooms = setup_rooms()
            player = Player(input("Name of your character: "), rooms[0])
            gameloop(player, rooms, settings)
        elif choice == "2":
            clear()
            print("These are your current settings, to adjust please edit the 'config.json' file.")
            print(settings)
            input("Press enter to continue...")
        elif choice == "3":
            clear()
            print("Checking for save file...")
            if savemanager.check_for_savefile():
                if input("Game file found! Do you want to load it? (y/n): ").lower() == "y":
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
    # Room setup
    victoryroom = Room(actions=["backward"], name="endroom", introtext="VICTORY!", is_victory=True)
    secondroom = Room(actions=["backward", "forward"], name="secondroom", introtext="Second Room")
    startroom = Room(actions=["forward"], name="startroom", introtext="You get randomly put into a dark. Cave? Well, "
                                                                      "it looks like a cave")

    rooms = [startroom, secondroom, victoryroom]
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
def gameloop(player, rooms, settings, savedgame=False):
    if savedgame:
        current_room = player.room
        current_room.intro_text()
    else:
        current_room = rooms[0]
        current_room.intro_text()
    while player.is_alive() and not player.victory:
        savemanager.save(player, rooms)
        current_room = player.room
        action = choice()
        if action in current_room.actions:
            player.do_action(action)
        elif action == "inv":
            player.print_inventory()
        elif action == "stat":
            player.print_stats()
        elif action == "debug" and settings["debug_mode"]:
            print(current_room.actions)
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
                    print(f"Room name: {current_room.name}")
                    print(f"Actions: {current_room.actions}")
                    print(f"Next room: {current_room.next_room}")
                    print(f"Last room: {current_room.last_room}")
                    print(f"IsVictory: {current_room.is_victory}")
                    print(f"Room Looted: {current_room.roomlooted}")
                elif command == "leave":
                    print("Leaving DEBUG mode")
                    break
                elif command == "help-debug":
                    valid_commands = ['leave', 'room', 'goto', 'room-info']
                    for command in valid_commands:
                        print("==> " + command)
        else:
            print("Not a legal action")
    if player.victory:
        with open("endcredits.txt", 'r') as f:
            text = f.readlines()
            for line in text:
                print(line)
                time.sleep(1)
            input("Press any key to continue...")


def helpmenu():
    possible_actions = ['forward', 'backward', 'take', 'drop']
    print("[====== HELP MENU ======]")
    print("Game wide possible actions:\n")
    for action in possible_actions:
        print("=> " + action)
    print("\n[=======================]")


def choice(message: str = None):
    yes = ["yes", "y"]
    while True:
        if message:
            choice = str(input(f'{message} > ')).lower()
        else:
            choice = str(input(f'> ')).lower()

        if choice == "help":
            helpmenu()
        elif choice == "exit":
            if input("Are you sure you want to quit? > ") in yes:
                sys.exit()
        else:
            break

    return choice


def prompt(message: str, *options):
    print(f'''

{message}

    ''')
    i = 0
    for option in options:
        i += 1
        print(f"[{i}] {option}\n\n")
    print("Pick one of the options: ")

    return choice()


if __name__ == '__main__':
    main()
