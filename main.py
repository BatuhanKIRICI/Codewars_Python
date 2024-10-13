n = int(input())

emp_list = []

for _ in range(0, n):
    if n > 0:
        n -= 1
        emp_list.append(n)

emp_list.reverse()

for x in emp_list:
    print(x * x)
