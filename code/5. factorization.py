# Title: Prime Factorization
# Created by Devender Singh

def prime_factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

number = int(input("Enter a number: "))
factors = prime_factorization(number)
print("Prime Factors:", factors)

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
