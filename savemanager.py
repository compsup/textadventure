import json

saveFile = "savefile.json"
def load_savefile():
    try:
        with open(saveFile, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                save_file()
                data = json.load(f)
    except FileNotFoundError:
        save_file()
        with open(saveFile, "r") as f:
            data = json.load(f)
    return data

def save_file():
    with open(saveFile, "w") as f:
        jsonConfig = json.dump("{}", f, indent=2)

def get_value(value:str):
    data = load_savefile()
    return data[value]
def set_value(key:str, value):
    data = load_savefile()
    data[key] = value
    return True

