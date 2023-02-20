
a = int(input("pick a numerator"))
b = int(input("pick a denominator"))
try:
    print(a / b)
except (ZeroDivisionError, RecursionError):
    print("Program Terminating")
