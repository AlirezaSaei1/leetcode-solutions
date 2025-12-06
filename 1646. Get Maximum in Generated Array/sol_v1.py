class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = []
        nums.append(0)
        nums.append(1)

        if n == 0:
            return 0

        i = 2
        while i <= n:
            if i % 2 == 0:
                nums.append(nums[i//2])
            else:
                nums.append(nums[(i//2)] + nums[(i//2)+1])
            i+=1
        
        return max(nums)
        