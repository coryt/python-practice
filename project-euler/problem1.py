#Multiples of 3 and 5
""" If we list all the natural numbers below 10 that are
    multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
    multiples is 23. Find the sum of all the multiples of 3 or 5
    below 1000."""

import math

def print_multiples():
    max_iter = 1000
    multiples = [3, 5]

    sum = 0
    for count in range(0, max_iter):
        for item in multiples:
            if count % item == 0:
                sum += count
                break
    return sum

print print_multiples()
