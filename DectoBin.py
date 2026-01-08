
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
