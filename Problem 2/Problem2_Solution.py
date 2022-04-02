sum = 0
N = 4000000
fib1 = 1
fib2 = 2
while fib1 <= N:
    if fib1 % 2 == 0:
        sum += fib1
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3

print(f"The sum of the first {N} Fibonacci numbers is {sum}.")