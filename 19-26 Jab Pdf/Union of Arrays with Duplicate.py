a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2] 

# result_arr = []

# for i in a:
#     if i not in result_arr:
#         result_arr.append(i)

# for i in b:
#     if i not in result_arr:
#         result_arr.append(i)
arr = []
arr.extend(a)
arr.extend(b)
print(list(set(arr)))
# set_arr = set(arr)

# print(set_ar)
