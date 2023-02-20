# So, first we have to open the file.
#
# And we And we use that using the Python built in function called Open.
#
# Then the next step is to read in the file which we can do either
#
# one line at
#
# a time or we can actually try and read in the entire file in one go.
#
# Finally to close the file when we're done with it is the final step.

# For mac and linux based systems.
# jabber = open("/Users/sumow/OneDrive/Desktop/sample.txt", 'r')

# For windows based systems:
# jabber = open("C:/Users/sumow/IdeaProjects/file_IO/sample.txt", 'r')

# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#     print(line)

# jabber.close()

# Python has a with statement that was introduced initially in Python 2.5,
#
# and if an object supports a use of with, and a file does, then with
#
# will tidy everything up automatically once the object's no longer needed.

# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')
#
# with open("sample.txt", 'r') as jabber:
#     line = jabber.readlines()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()  # Produces a list of all lines in the text file.
# print(lines)
#
# for line in lines:
#     print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()  # Produces a list of all lines in the text file.
print(lines)

for line in lines[::-1]:
    print(line, end='')

# readline reads a single line from a file and returns a string.
#
# readlines reads the entire file and returns a list of the lines in question.


