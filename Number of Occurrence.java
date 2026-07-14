/*
Number of Occurrence
Given a sorted array arr[] and a number target, find the number of occurrences of target in given array. 
Examples:
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: target = 4 is not present in the given array so the output is 0.
Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
Output: 3
Explanation: target =
*/
class Solution {
    int countFreq(int[] arr, int target) {
        // code here
        int count = 0;
        int length = arr.length - 1;
        for(int i = 0 ; i<arr.length ; i++){
            if(target == arr[i]){
                count++;
            }
        }
        
        return count;
    }
}
