"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when the input is not a hole numbwer
2. When will a ZeroDivisionError occur?
When the user inputs a 0 for the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Technically yes, but all you could do was add your own error message warning against a 0 if it was inputted. Would it
realistic difference, no.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")