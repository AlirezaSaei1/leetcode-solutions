class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)

        for i in range(0, n, 2):
            arr = [nums[i+1]] * nums[i]
            result.extend(arr)
        
        return result