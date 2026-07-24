class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False] * 2048
        
        pair_xor_counts = [0] * 2048
        for j in range(n):
            val_j = nums[j]
            for k in range(j, n):
                pair_xor_counts[val_j ^ nums[k]] += 1
                
        for i in range(n):
            val_i = nums[i]
            for p_val in range(2048):
                if pair_xor_counts[p_val] > 0:
                    seen[val_i ^ p_val] = True
                    
        return sum(seen)