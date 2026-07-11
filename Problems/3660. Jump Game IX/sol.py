class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        
        prefix_max = [0] * n
        curr_max = 0
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            prefix_max[i] = curr_max
            
        suffix_min = [float('inf')] * n
        curr_min = float('inf')
        for i in range(n - 1, -1, -1):
            curr_min = min(curr_min, nums[i])
            suffix_min[i] = curr_min
            
        start = 0
        for i in range(n):
            if i == n - 1 or prefix_max[i] <= suffix_min[i + 1]:
                seg_max = prefix_max[i]
                for j in range(start, i + 1):
                    ans[j] = seg_max
                start = i + 1
                
        return ans