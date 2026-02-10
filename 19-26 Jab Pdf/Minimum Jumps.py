arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

def minJumpsRecur(i, arr):
    if i >= len(arr) - 1:
        return 0
    
    ans = 1000000000
    for j in range(i + 1, i + arr[i] + 1):
        val = minJumpsRecur(j, arr)
        if val != 1000000000:
            ans = min(ans, 1 + val)

    return ans

def minJumps(arr):
    ans = minJumpsRecur(0, arr)
    
    if ans == 1000000000:
        return -1
        
    return ans

if __name__ == "__main__":
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print(minJumps(arr))
