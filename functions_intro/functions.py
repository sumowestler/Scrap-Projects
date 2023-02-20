# import random
#
#
# def get_integer(prompt):
#     wrong = highest
#     while True:
#         temp = input()
#         if temp.isnumeric():
#             if int(temp) > wrong or int(temp) < 0:
#                 print("This number is invalid")
#             else:
#                 return int(temp)    # Return will act as a break
#                 # statement.
#
#
#
# highest = 1000
# answer = random.randint(1, highest)
# guess = 0
# print(answer)   # TODO: Remove after testing
#
# print("Please guess number between 1 and {}: ".format(highest))
#
# while guess != answer:
#     guess = get_integer(": ")
#
#     if guess == 0:
#         break
#     elif guess == answer:
#         print("Well done, you guessed it")
#     else:
#         if guess < answer:
#             print("Please guess higher")
#         else:
#             print("Please guess lower")
#
# def multiply(x,y):
#     result = x * y
#     return result
# #
# #
def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.
    A palindrome is a string that reads the same backwards as forwards.

    :param string: The string to check.
    :return: True if string is a palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()
#
#
# #
# #
# # word = input("Please enter a word choice").casefold()
# # if is_palindrome(word):
# #     print("{} is a palindrome".format(word))
# # else:
# #     print("{} is not a palindrome".format(word))
#
#
# def palindrome_sentence(sentence):
#     string = ""
#     for char in sentence:
#         if char.isalnum():
#             string += char
#     print(string)
#     return is_palindrome(string)

def fibonacci(n):
    """Return the 'n' th Fibonacci number, for positive 'n'."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 =result

    return result
for i in range(10):
    print(i, fibonacci(i))

# word = input("Please enter a word choice").casefold()
# if palindrome_sentence(word):
#     print("{} is a palindrome".format(word))
# else:
#     print("{} is not a palindrome".format(word))

# answer = multiply(10.5, 4)
# print(answer)
#
# forty_two =  multiply(6,7)
# print(forty_two)
#
# print()
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)
answer = multiply(18, 3)
print(answer)