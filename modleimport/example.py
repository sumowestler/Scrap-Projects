# # print(dir())    # You can use this to print a directory of all functions
# # # and methods in a module.
# # # print(dir(__builtins__)) # This is not the easiest to read. Use a for loop.
# #
# # for m in dir(__builtins__):
# #     print(m)
#
import shelve
#
# for obj in dir(shelve.Shelf):
#     if obj[0] != '_':
#         print(obj)
#
# shelve.Shelf

# The help function will deliver all of the needed documentation for a module.
help(shelve)