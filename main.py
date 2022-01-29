#### Default Imports ####
import os
import platform
import sys

import config
#### Module Imports ####
import items
import room
from player import Player

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


def main():
    print("Loading config...")
    config.load()
    clear()
    print(f'''
Version: {CURRENT_VERSION}
---------------------------------------------

TextAdventure - by compsup2

---------------------------------------------
    ''')
    choice = prompt("Select an option", "New Game", "Options", "Load a saved game")
    if choice == "1":
        clear()
        player = Player(input("Name of your character: "))
        current_room = room.StartingRoom()
        gameloop(player, current_room)


# Start of the game
def gameloop(player, current_room):
    print(current_room.intro_text())
    player.stats()
    player.inventory()
    while player.is_alive() and not player.victory:
        current_room.modify_player(player)
        action = choice()
        if action == "inv":
            player.inventory()
        elif action == "stat":
            player.stats()




def helpmenu():
    input("Press enter to continue...")
    pass


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
