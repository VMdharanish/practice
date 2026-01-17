"""Decimal to Binary Converte"""


class Solution:
    def decToBinary(self, n):
        if n == 0:
            return "0"

        fir = []
        while n > 0:
            temp = n % 2
            fir.append(str(temp))
            n //= 2

        fir.reverse()
        return "".join(fir)
"""
In java
class Solution {
    public String decToBinary(int n) {
        if (n == 0) {
            return "0";
        }

        StringBuilder result = new StringBuilder();

        while (n > 0) {
            int temp = n % 2;
            result.append(temp);
            n = n / 2;
        }

        // Reverse to get correct binary representation
        result.reverse();
        return result.toString();
    }
}
"""
