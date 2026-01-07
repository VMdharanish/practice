"""
Kadane's Algorithm
You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].
Note : A subarray is a continuous part of an array.
Examples:
Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.
Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray [-2] has the largest sum -2.
"""
class Solution:
    def maxSubarraySum(self, arr):
        high = arr[0]
        result = arr[0]
        for i in range(1,len(arr)):
            high = max(high+arr[i],arr[i])
            result = max(result,high)
        return result

"""
class Maximize{
    int kadane(int[] arr){
        int result = arr[0];
        int high = arr[0];
        for(int i = 0; i < arr.length ; i++ ){
            high = Math.max(high+arr[i], arr[i]);
            result = Math.max(high, result);
        }
        return result;
    }
    public static void main(String[] args) {
        int[] price =  {2, 3, -8, 7, -1, 2, 3};
        Maximize obj = new Maximize();
        System.out.println(obj.kadane(price));
    }
}
"""
