class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1, max2 = -1, -1
        max_index = -1

        for i, x in enumerate(nums):
            if x > max1:
                max2 = max1
                max1 = x
                max_index = i
            elif x > max2:
                max2 = x
        
        return max_index if max1 >= 2 * max2 else -1
