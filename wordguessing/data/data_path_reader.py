"""this is code that will read the data of lang.json
so the other codes can easily get access to it"""

import json

PATH = "/workspaces/WordGuessingGame/wordguessing/data/lang.json"

def open_file(path= PATH):
    """this method will open the json file and 
    give the data of it"""

    with open(path, mode='r', encoding="utf-8") as file:
        data = json.load(file)

        languages = data["langs"]
        paths = data["files_path"]

    return languages, paths

