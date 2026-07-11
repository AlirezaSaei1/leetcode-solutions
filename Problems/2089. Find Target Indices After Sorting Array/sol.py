class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n_small = 0
        count_target = 0
        
        for num in nums:
            if num < target:
                n_small += 1
            
            if num == target:
                count_target += 1
        
        return list(range(n_small, n_small + count_target))