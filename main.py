def narcissistic(value):
    value_str = str(value)

    splitted_value = list(value_str)
    total = 0

    for x in splitted_value:
        x = int(x)
        total += x ** (len(splitted_value))
    if total == value:
        return True
    else:
        return False


print(narcissistic(153))
