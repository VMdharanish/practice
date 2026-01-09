"""
Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the answer fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.
Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.
Input: arr[] = [2, 3, 4] 
Output: 24 
Explanation: For an array with all positive elements, the result is product of all elements
"""

class Solution:
	def maxProduct(self,arr):
		# code here
		n = len(arr)
		L2R = R2L = 1
		result = arr[0]
		for i in range(n):
		    if L2R == 0:
		        L2R =1
		    if R2L == 0:
		        R2L = 1
		    L2R = L2R*arr[i]
		    
		    j = n - i - 1
		    R2L = R2L*arr[j]
		    
		    result = max(result,L2R,R2L)
		return result
