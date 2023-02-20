def func(p1, p2, *args, k,
         **kwargs):  # in the func function, p1 and p2 are positional parameters. args is a var positional parameter. k is a keyword parameter, arguments must be passed with a keyword. kwargs is a var keyword parameter. They appear in the proper order.
    print("positional-or-keyword:...{}, {}".format(p1, p2))
    print("var-positional (*args):...{}".format(args))
    print("keyword:..................{}".format(k))
    print("var-keyword:..............{}".format(kwargs))


func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)
# 1 and 2 are the positional arguments. 3, 4, and 5 are considered
# arguments and bundled together as a tuple. 6 is bound to k. This is
# important as it pertains to the order of arguments, python would not
# know to stop bundling *args unless keyword cam after.

def sum_numbers(*args: int) -> int:
    """

    :param args: Numbers to be added
    :return: The sum of numbers to be added
    """
    x = 0
    for i in args:
        x += i
    return x

print(sum_numbers(1, 2, 3, 4, 5))
