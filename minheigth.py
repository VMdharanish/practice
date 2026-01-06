"""Given an array arr[] denoting heights of n towers and a positive integer k.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by k
Decrease the height of the tower by k
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by k for each tower. After the operation, the resultant array should not contain any negative integers.

Examples :

Input: k = 2, arr[] = [1, 5, 8, 10]
Output: 5
Explanation: The array can be modified as [1+k, 5-k, 8-k, 10-k] = [3, 3, 6, 8]. The difference between the largest and the smallest is 8-3 = 5."""


class Solution:
    def getMinDiff(self, arr, k):
        # code here
        n = len(arr)
        arr.sort()
        result = arr[n-1] - arr[0]
         
        for i in range(1,len(arr)):
            if arr[i] - k < 0:
                continue
            Min_height = min(arr[0] + k, arr[i] - k)
             
            Max_height = max(arr[i-1]+k,arr[n-1]-k)
             
            result = min(result, Max_height-Min_height)
            
        return result
