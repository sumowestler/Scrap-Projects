from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print("chicken: {}".format(chicken_quantity))

beans_quantity = pantry.setdefault("beans", 0)
print("beans : {}".format(beans_quantity))

ketchup_quantity = pantry.get("ketchup", 0)
print("ketchup: {}".format(ketchup_quantity))
# So the get method on line ten appears
#
# to be doing the same thing as setdefault on line six. The difference,
# though, is that set
#
# default doesn't just return the default value - it adds the key to
# the dictionary as well.
z_quantity = pantry.setdefault("zucchini", "eight")
print("zucchini: {}".format(z_quantity))
print()
print("'pantry' now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)
