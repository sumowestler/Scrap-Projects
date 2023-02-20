from contents import pantry, recipes

def add_shopping_item(data: dict, item: str, amount: int)-> None:
    """ Add a tuple containing 'item' and 'amount' to the 'data' dict."""
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount
    # The setdefault method returns the value from the dictionary,
    # if the key exists.
    #
    # If the key doesn't exist, it creates a new entry for the key,
    # assigns the default value to it


# Set default method.


print(pantry)
print(recipes)
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # Display a menu of recipes we know how to cook.
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print("{} - {}".format(key, value))

    choice = input(": ")

    if choice == "0":
        break
    # So we've transformed the data, so that the keys from recipes
    #
    # becomes the values in display_dict.
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print("You have selected {}".format(selected_item))
        print("Checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        shopping_list = {}
        for item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(item, 0)
            if required_quantity <= quantity_in_pantry:
                print("{} OK\t".format(item))
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print("You need to buy {} of {}"
                      .format(quantity_to_buy, item))
                shopping_list[item] = quantity_to_buy
        print("Here is your shopping list")
        print(shopping_list)
    # line 23 checks that the user's input is a valid key
    #
    # in the display_dict dictionary. If it is, we can proceed to check
    # the ingredients, and we'll do that next.
