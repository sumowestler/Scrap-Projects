def fizz_buzz(number: int) -> str:
    """

    :param number: The number to be entered
    :return: fizz, buzz, or fizz buzz
    """
    if number % 3 == 0 and number % 5 == 0:
        result = "fizz buzz"
        return result
    elif number % 3 == 0:
        result = "fizz"
        return result
    elif number % 5 == 0:
        result = "buzz"
        return result


input("Play FizzBuzz. Press ENTER to start")
print()
next_number = 0
while next_number < 99:  # While loops can be used to increment
    # numbers.
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Yor go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:  # else block can be used to execute code when a loop terminates normally.
    print("Well done, you have reached {}".format(next_number))
