class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = []
        nums.append(0)
        nums.append(1)

        maxx = 1

        if n == 0:
            return 0

        i = 2
        while i <= n:
            if i % 2 == 0:
                x = nums[i//2]
                nums.append(x)
                if x > maxx:
                    maxx = x
            else:
                x = nums[(i//2)] + nums[(i//2)+1]
                nums.append(x)
                if x > maxx:
                    maxx = x
            i+=1
        
        return maxx
        