def duplicate_count(text):
    # Your code goes here
    text_list = list(text.lower())

    set_1 = []
    set_2 = []

    for x in text_list:
        if x not in set_1:
            count = text_list.count(x)
            if count > 1:
                set_1.append(x)
    for y in text_list:
        count = text_list.count(y)
        if text_list.count(y) > 1:
            set_2.append(y)
    if len(set_1) == 0:
        print(f"{len(set_1)} # no characters repeats more than once")
    else:
        print(f"{len(set_1)} ")


duplicate_count("infinity")
