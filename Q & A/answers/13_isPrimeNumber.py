# Write a Python function that takes an integer as input and returns True if the number is prime, and False otherwise.

# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# In other words, a prime number is a number that cannot be divided evenly by any other number except 1 and itself.

import math


def is_prime(num: int):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for number in range(3, int(math.sqrt(num)) + 1, 2):
        if num % number == 0:
            return False
        return True


print(is_prime(1))   # expect False
print(is_prime(2))   # expect True
print(is_prime(17))  # expect True
print(is_prime(20))  # expect False
