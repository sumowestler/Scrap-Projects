import copy
animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

# Perform a shallow copy
# things = animals.copy()

# Perform a deep copy
things = copy.deepcopy(animals)
print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])

# A deep copy will also copy any objects that are contained in
# whatever you're copying.
#
# A shallow copy only copies references - it doesn't make copies of
# contained objects.
