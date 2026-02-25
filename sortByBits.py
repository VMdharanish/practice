def sortByBits(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))


# Example 1
arr1 = [0,1,2,3,4,5,6,7,8]
print(sortByBits(arr1))

# Example 2
arr2 = [1024,512,256,128,64,32,16,8,4,2,1]
print(sortByBits(arr2))
