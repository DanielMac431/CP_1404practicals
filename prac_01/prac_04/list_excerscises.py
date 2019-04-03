# numbers = []
# for i in range(0, 5):
#     number = int(input("Enter Number : "))
#     numbers.append(number)
# average = sum(numbers)/len(numbers)
# print("The first number is {}\nThe last number is {}\nThe smallest number is {}\nThe largest number is {}\n"
#       "The average number is {}".format(numbers[0], numbers[-1], min(numbers), max(numbers), average))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user = str(input("Enter Username: "))
if user in usernames:
    print("Access Granted")
else:
    print("Access Denied")
