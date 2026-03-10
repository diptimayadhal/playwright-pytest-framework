# To read data from config.json file

import json

def load_config():
    with open("config/config.json") as f:
        return json.load(f)