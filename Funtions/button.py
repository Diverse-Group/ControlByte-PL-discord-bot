import json


def save_button_info(custom_id, role_id, course):
    with open("Assets/buttons_data.json", "r+") as file:
        data = json.load(file)
        data[custom_id] = {"role_id": role_id, "course": course}
        file.seek(0)
        json.dump(data, file)


def get_button_info(custom_id):
    with open("Assets/buttons_data.json", "r") as file:
        data = json.load(file)
        return data.get(custom_id)
