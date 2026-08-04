class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        return sorted(list(set(range(min(nums), max(nums))) - set(nums)))