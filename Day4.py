def reverse(arr):
    left,right = 0,len(arr)
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
    return arr


