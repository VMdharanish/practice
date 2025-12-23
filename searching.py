"""Searching techinque using menuj bar method"""
'''linear seaching'''
class linear:
    def lin(self,arr,key):
        n = len(arr)
        for i in range(n):
            if arr[i] == key:
                return 1
        return -1

'''BInary seaching'''
class binary:
    def bina(self,arr,key):
        low,high=0,len(arr)
        while low<=high:
            mid = (low + high) //2
            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                low = mid + 1
            else:
                high = arr[mid] - 1
arr = list(input("Enter arr : "))
key = int(input("Enter key : "))
cc = int(input("1:linear search\n2:Binary search\n choicce : "))
if cc == 1:
    obj = linear()
    if obj.lin(arr,key):
        print(True)
    else:
        print(False)
else:
    obj = binary()
    if obj.bina(arr,key):
        print(True)
    else:
        print(False)

OUTPUT

Enter arr : [1,2,3,4,7,4,6,8,9,12,34]
Enter key : 7
1:linear search
2:Binary search
 choicce : 1
True
