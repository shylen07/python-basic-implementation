# Title: Collatz Sequence
# Created by Devender Singh

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

number = int(input("Enter a number: "))
sequence = collatz_sequence(number)
print("Collatz Sequence:", sequence)
