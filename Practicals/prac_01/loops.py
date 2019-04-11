# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()
#
# for i in range(0, 101, 10):
#     print(i, end=' ')
# for i in range(0, 100, 10):
#     print(i, end=' ')
# print()
#
# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()

number_of_stars = int(input("Number of Stars: "))
if number_of_stars > 0:
    for i in range(0, number_of_stars + 1, 1):
        for j in range(0, i, 1):
            print("*", end='')
        print()
else:
    print("Invalid Input")