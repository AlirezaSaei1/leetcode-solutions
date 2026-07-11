class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i, num in enumerate(nums):
            if num == 0:
                result[i] = num
            else:
                idx = (i + num) % n
                result[i] = nums[idx]
        
        return result