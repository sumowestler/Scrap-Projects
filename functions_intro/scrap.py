def sum_eo(n, t):
    summation = []
    if t == 'e':
        for number in range(0, n):
            if number % 2 == 0:
                summation.append(number)
    elif t == 'o':
        for number in range(0, n):
            if number % 2 != 0:
                summation.append(number)
    else:
        summation = [-1]
    return sum(summation)
