class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start_val = 1
        summ = 1
        for num in nums:
            summ += num

            if summ < 1:
                val = (1 - summ)
                start_val += val
                summ += val
        
        return start_val
