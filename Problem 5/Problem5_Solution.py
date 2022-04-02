def gcd(a, b):
    div = 1
    for d in range(1, min(a, b) + 1):
        if int(a) % d == 0 and int(b) % d == 0:
            div = d
    return div


mult = 1
N = 20
for n in range(1, N + 1):
    mult *= (n / gcd(mult, n))
    mult = int(mult)

print(f"The smallest number with each integer in {{1,..., {N}}} as a divisor is {mult}.")