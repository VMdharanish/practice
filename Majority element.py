"""
Majority Element-More Than n/3
Given an array arr[] consisting of n integers, the task is to find all the array elements which occurs more than floor(n/3) times.

Note: The returned array of majority elements should be sorted.

Examples:

Input: arr[] = [2, 2, 3, 1, 3, 2, 1, 1]
Output: [1, 2]
Explanation: The frequency of 1 and 2 is 3, which is more than floor n/3 (8/3 = 2).
Input:  arr[] = [-5, 3, -5]
Output: [-5]
Explanation: The frequency of -5 is 2, which is more than floor n/3 (3/3 = 1).
Input:  arr[] = [3, 2, 2, 4, 1, 4]
Output: []
Explanation: There is no majority element.
"""
class Solution:
    def findMajority(self, arr):
        
        co1 ,co2 = 0,0
        el1,el2 = -1,-1
       
        
        for i in arr:
            if el1 == i:
                co1 += 1
            elif el2 == i:
                co2 += 1
            elif co1 == 0:
                el1 = i
            elif co2 == 0:
                el2 = i
            else:
                co1 -=1
                co2 -= 1
            
            ans = []
            cn1,cn2 = 0,0
            for i in arr:
                if el1 == i:
                    cn1 += 1
                if el2 == i:
                    cn2 += 1
            n = len(arr)
            if cn1 > n/3:
                ans.append(el1)
            if cn2 > n/3 and el1 != el2:
                ans.append(el2)
            if len(ans) == 2 and ans[0] > ans[1]:
                ans[0],ans[1] = ans[1],ans[0]
            return ans
