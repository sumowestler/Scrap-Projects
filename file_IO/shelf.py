import shelve

# shelf is a method of dealing with objects that are too big for pickle to handle due to memory concerns.
# It acts as a dictionary where pickle works more like a list. The objects that ae shelved are stored in a
# dictionary instead of on the computer's memory.

# with shelve.open('Shelftest') as fruit:
#     fruit['orange'] = "a sweet, orange, citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour, yellow citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"
#
#     print(fruit['lemon'])
#     print(fruit['grape'])

# print(fruit)

# If you want to keep your shelve active, you must close it manually.
fruit = shelve.open('Shelftest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

print(fruit['lemon'])
print(fruit['grape'])
fruit["lime"] = "great with tequila"

for snack in fruit:
    print(snack + ": " + fruit[snack])

fruit.close()   # shelf must be closed manually.

print(fruit)
