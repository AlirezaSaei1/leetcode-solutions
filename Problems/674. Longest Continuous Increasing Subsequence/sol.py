class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cur_len = 1
        max_len = 1

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len
                cur_len = 1
        
        return max(max_len, cur_len)