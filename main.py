# import math
# import os
# import random
# import re
# import sys

total = 0


def solve(meal_cost, tip_percent, tax_percent):

    total = (
        meal_cost + (meal_cost * tip_percent / 100) + (meal_cost * tax_percent / 100)
    )
    total = round(total)

    print(total)


if __name__ == "__main__":
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
