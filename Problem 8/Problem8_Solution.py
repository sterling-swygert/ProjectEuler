file1 = open(r"NumberGrid.txt","r")
grid_as_lists = []
oggrid = file1.readlines()
N = 13
for n in range(0, len(oggrid)):
    numstring = oggrid[n]
    for k in range(0, len(numstring) - 1):
        grid_as_lists.append(int(numstring[k]))

bigprod = 0
for n in range(0, len(grid_as_lists) - N):
    prod = 1
    for k in range(0, N):
        prod *= grid_as_lists[n + k]
    if prod > bigprod:
        bigprod = prod

print(f"The {N} adjacent digits with the largest product have a product of {bigprod}.")
