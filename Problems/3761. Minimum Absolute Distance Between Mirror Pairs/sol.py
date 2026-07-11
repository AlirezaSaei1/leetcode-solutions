class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        min_dist = float('inf')
        seen = {}

        for j in range(len(nums)):
            cur = nums[j]
            if cur in seen:
                dist = j - seen[cur]
                if dist < min_dist:
                    min_dist = dist
            
            temp = cur
            rev = 0
            while temp > 0:
                rev = rev * 10 + (temp % 10)
                temp //= 10
            
            seen[rev] = j
            
        return int(min_dist) if min_dist != float('inf') else -1

