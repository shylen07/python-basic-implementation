# Title: Fibonacci Sequence
# Created by Devender Singh

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

length = int(input("Enter the length of Fibonacci sequence: "))
fib_sequence = fibonacci(length)
print("Fibonacci Sequence:", fib_sequence)
