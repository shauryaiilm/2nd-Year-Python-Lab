org_array = [1, 4, 3, 2, 6, 5]

first = 0
second = len(org_array)-1

while(first<second):
    org_array[first], org_array[second] = org_array[second], org_array[first]
    second -= 1
    first += 1


print(org_array)
