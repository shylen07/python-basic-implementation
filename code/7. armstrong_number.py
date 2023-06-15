# Title: Armstrong Number Checker
# Created by Devender Singh

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == n

number = int(input("Enter a number: "))
if is_armstrong(number):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

