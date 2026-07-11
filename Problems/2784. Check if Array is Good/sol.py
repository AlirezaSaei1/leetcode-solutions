class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        perm = list(range(1, n))
        perm.append(n-1)

        return perm == sorted(nums)