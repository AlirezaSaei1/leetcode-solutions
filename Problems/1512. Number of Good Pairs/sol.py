class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        total = 0
        for val in count.values():
            total += val * (val - 1) // 2
        
        return total