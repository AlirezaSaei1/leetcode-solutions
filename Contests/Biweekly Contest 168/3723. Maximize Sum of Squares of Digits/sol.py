class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        
        digits = []
        for i in range(num):
            tmp = min(sum, 9)
            digits.append(str(tmp))
            sum -= tmp

        return ''.join(digits)
            