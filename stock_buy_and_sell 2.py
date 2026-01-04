"""Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by
buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.

Examples:

Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: You can buy the stock on day 2 at price = 1 and sell it on day 5 at price = 9. Hence, the profit is 8."""

class Solution:
    def maximumProfit(self, prices):
        # code here
        small = prices[0]
        result = 0
        for i in range(1,len(prices)):
            small = min(small,prices[i])
            result = max(result,prices[i] - small)
        return result

""" Same program in Java"""
"""

class stock{
    public static void main(String[] args) {
        int[] price =  {7, 10, 1, 3, 6, 9, 2};
        int min = price[0];
        int result = 0;
        for (int i =0 ; i<price.length ; i++){
            min = Math.min(min, price[i]);
            result = Math.max(result, price[i] - min);
        }
        System.out.println("Result = "+result);
    }
}
"""
