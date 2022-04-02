biggest = 0
for n in range(100, 1000):
    for k in range(n, 1000):
        numstring = str(n * k)
        munstring = ""
        for j in range(1, len(numstring) + 1):
            munstring += numstring[-j]
        if (numstring == munstring):
            big = n * k
            if big > biggest:
                biggest = big

print(f"The largetst palindrome that is a product of two 3-digit numbers is {biggest}.")