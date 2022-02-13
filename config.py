import json
import sys

configFileName = "config.json"
defaultConfig = {
    "configVersion": 0,
    "debug_mode": False,
}


def load():
    try:
        with open(configFileName, "r") as f:
            try:
                settings = json.load(f)
            except json.JSONDecodeError:
                create()
                settings = json.load(f)
    except FileNotFoundError:
        create()
        with open(configFileName, "r") as f:
            settings = json.load(f)
    if settings["configVersion"] < defaultConfig["configVersion"]:
        print("WARNING: Config file is newer then the current one")
        if input("Remove current config and re-install newer version? (y/n): ") == "y":
            settings.update(defaultConfig)
            create()
        else:
            print("Unable to proceed due to config most likely breaking program.")
            input("Press any key to continue...")
            sys.exit()

    return settings


def create():
    with open(configFileName, "w") as f:
        json.dump(defaultConfig, f, indent=2)
