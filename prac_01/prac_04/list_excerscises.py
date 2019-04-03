numbers = []
for i in range(0, 5):
    number = int(input(("Enter Number : ")))
    numbers.append(number)
average = sum(numbers)/len(numbers)
print("The first number is {}\nThe last number is {}\nThe smallest number is {}\n The largest number is {}\n The average number is {}".format(numbers[0], numbers[-1], min(numbers), max(numbers), average ))