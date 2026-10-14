class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        n9 = sum // 9
        rem = sum % 9
        
        if rem > 0:
            n0 = num - n9 - 1
            return "9" * n9 + str(rem) + "0" * n0
        else:
            n0 = num - n9
            return "9" * n9 + "0" * n0