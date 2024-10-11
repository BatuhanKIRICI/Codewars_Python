def dig_pow(n, p):
    # your code

    total = 0

    n = list(str(n))

    for x in n:

        total += int(x) ** p
        p += 1

    return -1


dig_pow(46288, 3)
