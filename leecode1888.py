'''
1888. Minimum Number of Flips to Make the Binary String Alternating
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
'''
class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        
        doubled_s = s + s
        
        target1 = "" 
        target2 = ""  
        for i in range(2 * n):
            if i % 2 == 0:
                target1 += '0'
                target2 += '1'
            else:
                target1 += '1'
                target2 += '0'
        
        min_flips = float('inf')
        flips1 = flips2 = 0
        
        for i in range(n):
            if doubled_s[i] != target1[i]:
                flips1 += 1
            if doubled_s[i] != target2[i]:
                flips2 += 1
        
        min_flips = min(flips1, flips2)
        
        for i in range(n, 2 * n):
            if doubled_s[i - n] != target1[i - n]:
                flips1 -= 1
            if doubled_s[i - n] != target2[i - n]:
                flips2 -= 1
            
            if doubled_s[i] != target1[i]:
                flips1 += 1
            if doubled_s[i] != target2[i]:
                flips2 += 1
            
            min_flips = min(min_flips, flips1, flips2)
        
        return min_flips
        
