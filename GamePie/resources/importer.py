import json
from buildInfo import buildInfo
def import_json(file_path:str):
    path = buildInfo["path"]
    try:
        with open(path + file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file '{path + file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")