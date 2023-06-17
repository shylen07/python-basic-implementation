# Title: Reverse of a Number
# Created by Devender Singh

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

number = int(input("Enter a number: "))
print("Reversed Number:", reverse_number(number))
