class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        val_idx = defaultdict(list)
        for i, n in enumerate(nums):
            val_idx[n].append(i)
        
        arr = [0] * len(nums)
        
        for val in val_idx:
            indices = val_idx[val]
            m = len(indices)
            if m <= 1:
                continue
            
            total_sum = sum(indices)
            prefix_sum = 0
            
            for count_left, current_idx in enumerate(indices):
                count_right = m - 1 - count_left
                
                suffix_sum = total_sum - prefix_sum - current_idx
                left_dist = (count_left * current_idx) - prefix_sum
                right_dist = suffix_sum - (count_right * current_idx)
                
                arr[current_idx] = left_dist + right_dist
                prefix_sum += current_idx
                
        return arr