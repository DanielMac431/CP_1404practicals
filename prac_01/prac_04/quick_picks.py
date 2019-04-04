
import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    number_of_lines = int(input("How many quick picks: "))
    while number_of_lines < 0:
        print("Please Enter a Valid Number!")
        number_of_lines = int(input("How many quick picks: "))

    for i in range(number_of_lines):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            if number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)

            quick_pick.append(number)
            quick_pick.sort()

        print(quick_pick)

main()