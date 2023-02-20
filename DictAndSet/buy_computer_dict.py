available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }
current_choice = None  # The default for when the users choice is
# not available.
computer_parts = {}  # Create an empty dictionary.

while current_choice != "0":
    if current_choice in available_parts:  # When you use in with a dictionary.
        # You are only checking the keys
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            print("Removing {}".format(chosen_part))
            computer_parts.pop(current_choice)
        else:
            print("Adding {}".format(chosen_part))
            computer_parts[current_choice] = chosen_part
            # Its already in so remove it.
        print("Your Dictionary now contains {}".format(computer_parts))
    else:
        if current_choice not in available_parts:
            for choice, part in available_parts.items():
                print(choice, part, sep=",")

    current_choice = input("> ")
# When you use in with a dictionary it checks the keys in the dictionary
# not, the values.
