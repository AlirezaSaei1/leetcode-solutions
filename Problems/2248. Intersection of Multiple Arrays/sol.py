class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common = set(nums[0]).intersection(*nums[1:])
        
        return sorted(list(common))