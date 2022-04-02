found = False
for a in range(1,1000):
    for b in range(1,1000-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            triple = (a,b,c)
            prod = a*b*c
            print(f"The only triplet (a,b,c) such that a^2 + b^2 = c^2 and a + b + c = 1000 is "
                  f"{triple} and the product a*b*c is {prod}.")
            found = True
            break
    if found == True:
        break