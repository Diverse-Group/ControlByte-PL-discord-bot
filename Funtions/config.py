import json

with open("config.json", "r") as f:
    config = json.load(f)


def get(key):
    return config[key]
