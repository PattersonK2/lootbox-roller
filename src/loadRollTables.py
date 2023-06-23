import json
import os

data_dict = {}


def load_roll_tables():
    json_dir = "/rollTables"

    whole_directory = os.listdir(json_dir)
    i = 0
    # Iterate over the JSON files in the directory
    for filename in whole_directory:
        i += 1
        if filename.endswith('.json'):  # Ensure only JSON files are considered
            file_path = os.path.join(json_dir, filename)

            # Read and parse the JSON file
            print(f"loading ({i}/{whole_directory.__len__})... {filename}")
            with open(file_path, 'r') as file:
                json_data = json.load(file)

            # Add the parsed data to the dictionary
            data_dict[filename] = json_data


def load_roll_table(quality):
    # TODO: remove opening files and do it all in one step.
    filename = f"{quality}.base.json"
    return data_dict[filename]
