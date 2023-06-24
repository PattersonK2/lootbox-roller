# Generate a random integer between 1 and 100
import random
from loadRollTables import load_roll_table


def roll_loot(quality, type="base", manual_rolls=False):
    data = load_roll_table(quality, type)
    random_number = random.randint(1, 100)

    if (manual_rolls):
        while True:
            user_input = input("Enter your roll (1-100): ")
            try:
                random_number = int(user_input)
                break
            except ValueError:
                print("Input is not a valid number.")

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
        if "rollTwice" == matched_item:
            return roll_loot(quality, type, manual_rolls) + roll_loot(quality, type, manual_rolls)
        if "|" in matched_item:
            pieces = matched_item.split("|")
            if len(pieces) == 2:
                prefix, subtype = pieces
                matched_item = prefix + \
                    roll_loot(quality, subtype, manual_rolls)
            elif len(pieces) == 3:
                prefix, middle, subtype = pieces
                matched_item = prefix + \
                    roll_loot(quality, middle, manual_rolls) + \
                    roll_loot(quality, subtype, manual_rolls)
            else:
                raise ValueError(
                    f"unhandled: incorrect number of '|' in {matched_item}")
        return matched_item
    else:
        print("No match found.")
        raise LookupError("Cannot find matched item for rolled number")
