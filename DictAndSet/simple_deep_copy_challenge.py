def simple_deep_copy(d: dict) -> dict:
    """

    :param d: A dictionary to be copied
    :return: A copy of that dictionary
    """
    d_copy = {}
    for key, value in d.items():
        d_copy[key] = value
    return d_copy


animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}
animals_copy = simple_deep_copy(animals)

print()

print(animals)
print(animals_copy)
