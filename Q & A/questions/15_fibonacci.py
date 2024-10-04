# 4. Fibonacci Sequence
# Write a function that generates the Fibonacci sequence up to a given number n. The Fibonacci sequence
# is defined as follows:
# - F(0) = 0
# - F(1) = 1
# - F(n) = F(n-1) + F(n-2) for n > 1
# The function should return an array containing the Fibonacci numbers up to the largest number less than
# or equal to n.

# Input: 10
# Output: [0, 1, 1, 2, 3, 5, 8]

def fibonacci(num):
    fib = [0, 1]
    while True:
        newFib = fib[-1] + fib[-2]
        if newFib > num:
            break
        fib.append(newFib)
    return fib


print(fibonacci(10))
