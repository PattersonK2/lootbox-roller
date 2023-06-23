from rollLoot import roll_loot


def select_lootbox():
    print("Select Lootbox to roll:")
    print("1. Bronze")
    print("2. Silver")
    print("3. Quality")

    # Prompt for user input
    while True:
        selection = input("Enter your selection (1-3): ")
        if selection in ['1', '2', '3']:
            return int(selection)
        else:
            print("Invalid input. Please enter a valid selection.")


# Call the function to prompt the user
user_selection = select_lootbox()

# Do something based on the user's selection
if user_selection == 1:
    print("Bronze selected.")
    roll_loot("bronze")
elif user_selection == 2:
    print("Silver selected.")
    roll_loot("silver")
elif user_selection == 3:
    print("Quality selected.")
    roll_loot("quality")
else:
    print(f"How TF was {user_selection} selected?!")
