class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target = total_sum % p

        if target == 0:
            return 0
        
        n = len(nums)
        res = n

        seen = {0: -1}
        curr = 0

        for i, x in enumerate(nums):
            curr = (curr + x) % p
            need = (curr - target) % p

            if need in seen:
                res = min(res, i - seen[need])

            seen[curr] = i

        return res if res < n else -1
        
