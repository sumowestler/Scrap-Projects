d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "IV": "four",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']
# The values method returns a view of the dictionary's values.

v = d.values()
print(v)

d[10] = "ten"

print("four" in v)
print("eleven" in v)

keys = list(d.keys())
values = list(v)
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print("{} was found in the key {}".format(d[key], key))

print()

for key, value in d.items():
    if value == "four":
        print("{} was found in the key {}".format(d[key], key))
# Code for "The dict "update" method" lecture
# d2 = {
#     7: "lucky seven",
#     10: "ten",
#     3: "this is the new three"
# }
#
# d.update(d2)
# for key, value in d.items():
#     print(key, value)
#
# # update method for dictionaries acts like the append method for lists. Lets you
# # add to a specific dictionary and fuse 2 dictionaries together. Note
# # that keys are unique, updating with the same key will result in a
# # new value replacing the old.
#
# print()
#
# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)

# Code for "The remaining "dict" methods lecture
# ***********************************************
# Fromkeys class method.
# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)
# fromkeys method is a useful way to create an initial dictionary,
# which your code will then change.
# Each key starts off with the default value 0, in this case.
# If you were creating an empty pantry, for example,
# this could be a good way to do it. The code would then change the amounts,
# when the cook entered how much they had of each item.

# # Keys method:
# keys = d.keys()
# print(keys)
# # Example:
# for item in d.keys():
#     print(item)
