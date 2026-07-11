class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        ones = num.bit_count()
        bits = num.bit_length()
        
        return ones + bits - 1