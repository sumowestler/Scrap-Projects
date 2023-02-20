# cities = ["Adelade", "Alice Springs", "Darwin", "Melbourne", " Sydney"]

# How to write to a file.
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

# cities = []
#
# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip())  # .strip method can be used to get
#         # rid of the new line character (\n) notation in the final printed
#         # product.
#
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda May", "2021", ((1, "Pulling the Rug"), (2, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("Imelda3.txt", "w") as imelda_file:
#     print(imelda, file=imelda_file)   # will write the text as a tuple, but cannot be read as one.
# need the eval function to turn the notation back to the way that it was.

with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
