class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        length = len(nums)

        while length != 1:
            pos = 0
            flag = True
            for i in range(0, length, 2):
                if flag:
                    nums[pos] = min(nums[i], nums[i+1])
                    flag = False
                else:
                    nums[pos] = max(nums[i], nums[i+1])
                    flag = True

                pos += 1

            length //= 2
        
        return nums[0]