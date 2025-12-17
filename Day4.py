def reverse(arr):
    left,right = 0,len(arr)
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
    return arr

#Remove duplicate values

def remove_duplicates(arr):
    if not arr:
        return 0
    s = 0
    for i in range(1,len(arr)):
        if arr[s] != arr[i]:
            arr[s],arr[i] = arr[i],arr[s]
            s+=1
    return s+1
arr = [1, 1, 2, 2, 3]
k = remove_duplicates(arr)
print(k, arr[:k])

