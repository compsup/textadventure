import json

configFileName = "config.json"
defaultConfig = {
    "difficulty": "normal",
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
    return settings


def create():
    with open(configFileName, "w") as f:
        json.dump(defaultConfig, f, indent=2)


