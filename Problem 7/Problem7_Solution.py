primes = [2]
N = 10001
n = 3
while len(primes) < N:
    prime = True
    for d in primes:
        if n % d == 0:
            prime = False
            break
    if prime == True:
        primes.append(n)
    n += 2

print(f"The {N}th prime is {primes[N - 1]}.")