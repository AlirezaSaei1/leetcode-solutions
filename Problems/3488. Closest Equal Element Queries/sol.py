class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        answer = []
        val_idx = defaultdict(list)

        for i, num in enumerate(nums):
            val_idx[num].append(i)

        answer = []
        for q_idx in queries:
            target_val = nums[q_idx]
            indices = val_idx[target_val]
            ni = len(indices)

            if ni <= 1:
                answer.append(-1)
                continue
            
            pos = bisect_left(indices, q_idx)
            idx_right = indices[(pos + 1) % ni]
            idx_left = indices[(pos - 1) % ni]
            
            dist_right = abs(q_idx - idx_right)
            dist_right = min(dist_right, n - dist_right)
            
            dist_left = abs(q_idx - idx_left)
            dist_left = min(dist_left, n - dist_left)
            
            answer.append(min(dist_right, dist_left))
            
        return answer