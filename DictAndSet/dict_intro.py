vehicles = {'dream': 'Honda 250T',
            'roadster': 'BMW R1100',
            'er5': 'Kawasaki ER5',
            'can-am': 'Bombardier Can-Am 250',
            'virago': 'Yamaha XV250',
            'tenere': 'Yamaha XV250',
            'jimny': 'Suzuki Jimni 1.5',
            'fiesta': 'Ford Fiesta Ghia 1.4'
            }  # Dictionaries use curly braces.

# Adding items to the dictionary. Notice that dictionaries don't have
# an append method. We assign the value to the dictionary, using it's
# key.

vehicles["starfighter"] = "Lockheed F-10"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# upgrade the Virago, changing a value in a dictionary using the same
# adding method.
vehicles["virago"] = "Yamaha XV535"
# How to delete from dictionary.
del vehicles["starfighter"]
# You can also use the .pop method. Removes item from dictionary.
# Returns value. Can be used for testing.
# If used on non-existent key values, will return error. Can set default
# value to what you want
vehicles.pop("f1", None)
result = vehicles.pop("f1", "No")
print(result)
print()

plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not prsent")
print(bike)
print()




my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

learner = vehicles.get('er5')
print(learner)  # get method is a method of calling information from a
# dictionary.

# So if the key doesn't exist, dot get will return none
#
# whereas indexing will crash with a key error, as you saw.
#
# The get method is useful when you're not sure if the key exists
# or not.
# Dictionaries can be iterated over.

# for key in vehicles:
#     print(key, vehicles[key], sep=", ")

# with dictionaries. We don't have to call enumerate,
# because dictionaries have the dot items method.

for key, value in vehicles.items():
    print(key, value, sep=", ")
