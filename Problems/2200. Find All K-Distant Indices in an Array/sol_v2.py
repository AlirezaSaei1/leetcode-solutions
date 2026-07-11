class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        indices = set()
        
        for i in range(n):
            if nums[i] == key:
                indices.update(range(max(0, i-k), min(n, i+k+1)))

        return list(indices)