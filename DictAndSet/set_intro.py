farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
# A Python set is enclosed in curly braces – just like a dictionary.
print(farm_animals)

for animal in farm_animals:
    print(animal)
# You cannot index into a set like you would a list because it is
# unordered.
print()
print("Indexing a sequence")
animals_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animals_list[3]
print(goat)

# print("Indexing a set is not possible")
# goats = farm_animals[3]

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}
if more_animals == farm_animals:
    print('The sets are equal')
else:
    print('The sets are different')
# The sets are equal. Python considers sets to be equal, if they
# contain the same items. Ordering is unimportant – it's the items
# contained in the set that count.