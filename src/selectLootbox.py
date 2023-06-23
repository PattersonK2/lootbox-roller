from rollLoot import roll_loot


def select_lootbox(quick_roll=None):
    choices = ['1', '2', '3']
    if quick_roll in choices:
        return int(quick_roll)
    print("Select Lootbox to roll:")
    print("1. Bronze")
    print("2. Silver")
    print("3. Quality")

    # Prompt for user input
    while True:
        selection = input("Enter your selection (1-3): ")
        if selection in choices:
            return int(selection)
        else:
            print("Invalid input. Please enter a valid selection.")


def user_interaction(quick_roll=None):
    # Call the function to prompt the user
    user_selection = select_lootbox(quick_roll)

    loot = ""
    # Do something based on the user's selection
    if user_selection == 1:
        print("Bronze selected.")
        loot = roll_loot("bronze")
    elif user_selection == 2:
        print("Silver selected.")
        loot = roll_loot("silver")
    elif user_selection == 3:
        print("Quality selected.")
        loot = roll_loot("quality")
    else:
        print(f"How TF was {user_selection} selected?!")

    print(f"You rolled a: {loot}")
