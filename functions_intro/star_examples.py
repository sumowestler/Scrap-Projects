# when you use an asterisk before an object,
# it unpacks the sequence.

numbers = (0, 1, 2, 3, 4, 5)


# print(numbers, sep=";")
# print(*numbers, sep=";")
# print(0, 1, 2, 3, 4, 5, sep=";")

# *args allows us to pass a variable number of arguments to functions.
def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()
# It can also be used to write functions which take no arguments.
