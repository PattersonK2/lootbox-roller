import json
import os

data_dict = {}


def load_roll_tables():
    json_dir = "rollTables"

    parent_directory = os.getcwd()
    path_to_json_files = os.path.join(parent_directory, "src", json_dir)
    whole_directory = os.listdir(path_to_json_files)
    i = 0
    # Iterate over the JSON files in the directory
    for filename in whole_directory:
        i += 1
        if filename.endswith('.json'):  # Ensure only JSON files are considered
            file_path = os.path.join(path_to_json_files, filename)

            # Read and parse the JSON file
            print(
                f"loading ({i}/{len(whole_directory)})... {filename}")
            with open(file_path, 'r') as file:
                json_data = json.load(file)

            # Add the parsed data to the dictionary
            data_dict[filename] = json_data


def load_roll_table(quality, type="base"):
    # TODO: remove opening files and do it all in one step.
    filename = f"{quality}.{type}.json"
    allfile = f"all.{type}.json"
    if filename in data_dict:
        return data_dict[filename]
    elif allfile in data_dict:
        return data_dict[f"all.{type}.json"]
    else:
        raise NotImplementedError(
            f"Couldn't find file '{filename}' or '{allfile}', please make one of them")
