arr = [2, 3, -8, 7, -1, 2, 3]

maxsum = 0
tempsum = 0

for i in range(len(arr)):
    tempsum += arr[i]
    maxsum = max(maxsum,tempsum)
    if tempsum < 0:
        tempsum = 0


print(maxsum)
