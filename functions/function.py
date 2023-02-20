def python_food():
    width = 60
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# def center_text(text: str) -> str:
#     """
#     Accepts a string and returns a centered version.
#     :param text: The string to be accepted
#     :return: centered text
#     """
#     text = str(text)
#     left_margin = 80 - len(text) // 2
#     print(" " * left_margin, text)

# Making a modification for multiple arguments.

# def center_text(*args, sep=' ', end='\n', file=None,
#                 flush=False):  # Use * to modify the function for multiple arguments
#     """
#     Accepts a string and returns a centered version.
#     :param text: The string to be accpted
#     :return: centered text
#     """
#     text = ""
#     for arg in args:
#         text += str(arg) + sep
#     left_margin = 80 - len(text) // 2
#     print(" " * left_margin, text, end=end, file=file, flush=flush)

# Getting rid of the print function for better functionality

def center_text(*args, sep=' '):  # Use * to modify the function for multiple arguments
    """
    Accepts a string and returns a centered version.
    :param text: The string to be accpted
    :return: centered text
    """
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = 80 - len(text) // 2
    return " " * left_margin, text


# with open("centered", mode='w') as centered_file:
 # Call the function.
print(center_text("spam and eggs"))
print(center_text("spam, spam and eggs"))
print(center_text("spam, spam, spam and eggs"))
print(center_text(12))
print(center_text('first', 'second', 3, 4, 'spam', sep=":"))
print()
