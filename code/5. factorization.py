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
