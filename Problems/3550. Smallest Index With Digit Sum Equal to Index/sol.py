class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        limit = min(len(nums), 28)

        for i in range(limit):
            n = nums[i]
            d_sum = 0
            while n > 0:
                d_sum += n % 10
                n //= 10
            
            if d_sum == i:
                return i

        return -1