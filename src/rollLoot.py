# Generate a random integer between 1 and 100
import random
from loadRollTables import load_roll_table


def roll_loot(quality):
    data = load_roll_table(quality)
    random_number = random.randint(1, 100)

    # Find the matching item in the JSON data
    matched_item = None

    for key in data:
        start, end = map(int, key.split('-'))
        if start <= random_number <= end:
            matched_item = data[key]
            break

    # Print the result
    print("Random Number:", random_number)
    if matched_item is not None:
        print("Matched Item:", matched_item)
        return matched_item
    else:
        print("No match found.")
        raise LookupError("Cannot find matched item for rolled number")
