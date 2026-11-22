/*
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
*/
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int rl = 0;
        int ru = matrix.length - 1;
        int cl = 0;
        int cu = matrix[0].length - 1;
        while (rl <= ru && cl <= cu) {
            for (int i = cl; i <= cu; i++) {
                result.add(matrix[rl][i]);
            }
            rl++;
            for (int i = rl; i <= ru; i++) {
                result.add(matrix[i][cu]);
            }
            cu--;
            if (rl <= ru) {
                for (int i = cu; i >= cl; i--) {
                    result.add(matrix[ru][i]);
                }
                ru--;
            }
            if (cl <= cu) {
                for (int i = ru; i >= rl; i--) {
                    result.add(matrix[i][cl]);
                }
                cl++;
            }
        }
        return result;
    }
}
