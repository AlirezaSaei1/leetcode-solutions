class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mn, mx = float('inf'), float('-inf')
        for num in nums:
            if num < mn:
                mn = num
            if num > mx:
                mx = num
        return max(0, mx - mn - 2 * k)
