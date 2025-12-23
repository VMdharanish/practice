'''linear seaching'''
class linear:
    def lin(self,arr,key):
        n = len(arr)
        for i in range(n):
            if arr[i] == key:
                return 1
        return -1
obj = linear()
arr = [1,2,3,4,7,4,6,8,9,12,34]
key = 2
if obj.lin(arr,key):
    print(True)
else:
    print(False)
