class Solution:
    def maxProduct(self, n: int) -> int:
        max1, max2 = float('-inf'), float('-inf')

        while n > 0:
            digit = n % 10
            n //= 10

            if digit >= max1:
                if max1 >= max2:
                    max2 = max1
                max1 = digit
            elif digit >= max2:
                max2 = digit
            
        return max1 * max2