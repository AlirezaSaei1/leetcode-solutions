class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        best = 1
        i = 0
        for j in range(n):
            while nums[j] > nums[i] * k:
                i += 1
            best = max(best, j - i + 1)
        return n - best