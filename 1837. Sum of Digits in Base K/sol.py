class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n == 0:
            return "0"

        sum_digits = 0
        while n > 0:
            n, rem = divmod(n, k)
            sum_digits += rem

        return sum_digits