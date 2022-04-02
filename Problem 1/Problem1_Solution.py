sum = 0
N = 1000

for n in range(0, N):
    if n % 3 == 0:
        sum += n
    elif n % 5 == 0:
        sum += n

print("The sum of all positive numbers divisible by 3 or 5 less than", N, "is", sum)