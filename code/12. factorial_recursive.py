# Title: Recursive Factorial
# Created by Devender Singh

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

number = int(input("Enter a number: "))
print("Factorial:", factorial_recursive(number))
