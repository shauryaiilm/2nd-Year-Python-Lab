org_array = [1, 4, 3, 5, 8, 6]
minele = org_array[0]
maxele = org_array[-1]

for i in org_array:
    minele = min(i,minele)
    maxele = max(i,maxele)


print("Minimum value is:", minele)
print("Maximum value is:", maxele)
