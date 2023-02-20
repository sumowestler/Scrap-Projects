# # numbers = {}
# numbers = {*""}  # Producing an empty set
# numbers = set()
# print(numbers, type(numbers))
# # To add numbers to a set, use the add function.
# numbers.add(1)
# print(numbers)
#
# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value: "))
#     numbers.add(next_value)
# print(numbers)

# Sets can be used to remove duplicate data.
data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# Create a set from the list to remove duplicates.
unique_data = set(data)
print(unique_data)

# Create a list of unique colors, keeping the order in which they
# appeared.
unique_data = list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data))
