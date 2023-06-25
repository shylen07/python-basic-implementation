# Title: Largest Palindrome
# Created by Devender Singh

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome(limit):
    largest = 0
    for i in range(limit, 0, -1):
        for j in range(limit, 0, -1):
            product = i * j
            if is_palindrome(product) and product > largest:
                largest = product
    return largest

limit = int(input("Enter a limit: "))
result = largest_palindrome(limit)
print("Largest Palindrome:", result)

