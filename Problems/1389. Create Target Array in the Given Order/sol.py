class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            result.insert(index[i], nums[i])
        
        return result