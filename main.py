n = int(input())

result = ""

li = []

for x in range(1, (n + 1)):

    li.append(x)
    n -= 1

numbers = [str(item) for item in li if isinstance(item, (int))]

result = str("".join(numbers))


print(result)
