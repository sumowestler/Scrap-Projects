small_ints = set(range(21))
print(small_ints)

# small_ints.clear()  # Clear function deletes the contents of a set.
# print(small_ints)

small_ints.discard(10)
small_ints.remove(11)   # these two method remove items from a set.
print(small_ints)

small_ints.discard(99)
print(small_ints)

small_ints.remove(99)   # Will crash the program if removed item is not
# in set. Can be used to check if item exists.
print(small_ints)
 