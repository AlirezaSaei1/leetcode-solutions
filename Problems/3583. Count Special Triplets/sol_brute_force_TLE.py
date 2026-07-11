class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (nums[i] == nums[j] * 2) and (nums[k] == nums[j] * 2):
                        seen.add((i, j, k))
        
        return len(seen)