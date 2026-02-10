nums = [1,3,5,6]
target = 5 

def searchEle():
    low = 0
    high = len(nums)-1
    idx = len(nums)

    while (low <= high):
        mid = low + (high-low)//2
        if nums[mid] >=  target:
            idx = min(idx,mid)
            high = mid-1
        else:
            low = mid+1
    
    return idx


print(searchEle())
