if __name__ == "__main__":

    list_1 = []
    list_2 = []
    list_3 = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        list_1.append([name, score])

    # print(list_1)

    for item in list_1:
        list_2.append(item[1])

    list_2 = sorted(set(list_2))

    # print(list_2)

    for item in list_1:
        if item[1] == list_2[1]:
            list_3.append(item[0])

    list_3 = sorted(set(list_3))

    for item in list_3:
        print(item)
