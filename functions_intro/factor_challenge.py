def factorial(number: int) -> int:
    """

    :param number: number to be factored
    :return: the factored number
    """
    factor = 1
    for i in range(1, number + 1):
        factor *= i
    return factor


for number in range(0, 1001):
    print(number, factorial(number))
