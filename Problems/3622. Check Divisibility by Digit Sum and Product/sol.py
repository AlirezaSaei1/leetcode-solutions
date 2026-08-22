class Solution:
    def checkDivisibility(self, n: int) -> bool:
        dsum = 0
        dprod = 1
        tmp = n

        while tmp > 0:
            digit = tmp % 10

            dsum += digit
            dprod *= digit

            tmp //= 10

        return n % (dprod + dsum) == 0