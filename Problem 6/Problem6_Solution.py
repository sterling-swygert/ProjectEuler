norm_sum = 0
sqsum = 0
N = 100
for n in range(1, N + 1):
    norm_sum += n
    sqsum += n ** 2

print(f"The difference between the squared-sum and sum-squared of the first {N} "
      f"positive integers is {abs(norm_sum ** 2 - sqsum)}.")