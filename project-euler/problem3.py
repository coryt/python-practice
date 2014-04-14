#Largest prime factor
"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
def prime_factors(n):
    i = 2
    while n % i != 0 and i < n:
        i += 1

    if i < n:
        return prime_factors(n / i)
    else:
        return n

print prime_factors(13195)
