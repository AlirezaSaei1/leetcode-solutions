class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        def dist(i, j, k):
            return abs(i - j) + abs(j - k) + abs(k - i)

        min_dist = float('inf')
        n = len(nums)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if (i != j) and (i != k) and (j != k):
                        if nums[i] == nums[j] == nums[k]:
                            min_dist = min(min_dist, dist(i, j, k))
        
        return min_dist if min_dist != float('inf') else -1
