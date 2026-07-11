class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0

        for i in nums:
            if i == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        
        return max(max_count, count)
