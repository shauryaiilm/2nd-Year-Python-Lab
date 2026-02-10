arr = [1, 2, 3, 4, 5] 

lastele = arr[-1]
arr.remove(arr[-1])
arr.insert(0,lastele)



print(arr)
