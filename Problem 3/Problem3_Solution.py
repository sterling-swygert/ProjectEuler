N = 600851475143
M = N

primes = [2]
big = 1
n = 2

while M >= primes[-1]:
    if M % n == 0:
        M = M / n
        comp = False
        for p in primes:
            if n % p == 0:
                comp = True
                n += 1
                break
        if comp == False:
            primes.append(n)
            big = n
    else:
        n = n + 1

print(f"The largest prime factor of {N} is {big}.")