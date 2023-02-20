albums = [("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))

for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year {}"
          .format(name, artist, year))



# title, artist, year, = metallica
# print(title)
# print(artist)
# print(year)  # tuple items can be made into variables this way.
#
# table = ("Coffee table", 200, 100, 75, 3450)
# print(table[1] * table[2])  # These variables can then be manipulated.
#
# name, length, width, height, price = table
# print(length * width)
