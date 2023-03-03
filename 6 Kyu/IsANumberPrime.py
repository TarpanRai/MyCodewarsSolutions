# Define a function that takes an integer argument and
# returns a logical value true or false depending on if the integer is a prime.


import math


def is_prime(n):
    # Edge Case
    if n <= 1 or n == 4 or n == 6 or n == 8:
        return False
    if n == 2:
        return True
    # Use math function
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
