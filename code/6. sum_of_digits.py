# Title: Sum of Digits
# Created by Devender Singh

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

number = int(input("Enter a number: "))
print("Sum of Digits:", sum_of_digits(number))

