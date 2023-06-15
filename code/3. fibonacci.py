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

# Commit on 2023-04-22 00:00:00 +0530

# Commit on 2023-04-23 00:00:00 +0530

# Commit on 2023-04-24 00:00:00 +0530

# Commit on 2023-04-26 00:00:00 +0530

# Commit on 2023-04-27 00:00:00 +0530

# Commit on 2023-04-28 00:00:00 +0530

# Commit on 2023-04-29 00:00:00 +0530

# Commit on 2023-04-30 00:00:00 +0530

# Commit on 2023-05-02 00:00:00 +0530

# Commit on 2023-05-03 00:00:00 +0530

# Commit on 2023-05-04 00:00:00 +0530

# Commit on 2023-05-05 00:00:00 +0530

# Commit on 2023-05-06 00:00:00 +0530

# Commit on 2023-05-07 00:00:00 +0530

# Commit on 2023-05-09 00:00:00 +0530

# Commit on 2023-05-10 00:00:00 +0530

# Commit on 2023-05-11 00:00:00 +0530

# Commit on 2023-05-12 00:00:00 +0530

# Commit on 2023-05-13 00:00:00 +0530

# Commit on 2023-05-15 00:00:00 +0530

# Commit on 2023-04-22 00:00:00 +0530

# Commit on 2023-04-22 00:00:00 +0530

# Commit on 2023-04-23 00:00:00 +0530

# Commit on 2023-04-24 00:00:00 +0530

# Commit on 2023-04-26 00:00:00 +0530

# Commit on 2023-04-27 00:00:00 +0530

# Commit on 2023-04-28 00:00:00 +0530
