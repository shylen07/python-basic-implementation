# Title: Pythagorean Triplet Checker
# Created by Devender Singh

def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))
if is_pythagorean_triplet(a, b, c):
    print("Pythagorean Triplet")
else:
    print("Not Pythagorean Triplet")
