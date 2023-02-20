import shelve

with shelve.open("bike") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 Dream"
    # bike["colour"] = "red"
    # bike["Engine_size"] = 250
    for key in bike:
        print(key)

    print('*' * 40)

    print(bike["Engine_size"])
    print(bike["colour"])

# just like a dictionary we can iterate through the keys in the
# shelve and print them out.
# we can also use del
