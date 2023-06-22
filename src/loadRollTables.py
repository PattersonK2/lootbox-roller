import json
import os

data_dict = {}


def load_roll_tables():
    json_dir = "/rollTables"

    # Iterate over the JSON files in the directory
    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):  # Ensure only JSON files are considered
            file_path = os.path.join(json_dir, filename)

            # Read and parse the JSON file
            with open(file_path, 'r') as file:
                json_data = json.load(file)

            # Add the parsed data to the dictionary
            data_dict[filename] = json_data


def load_roll_table(quality):
    # TODO: remove opening files and do it all in one step.
    with open(f'rollTables/{quality}.base.json', 'r') as file:
        data = json.load(file)

    return data
