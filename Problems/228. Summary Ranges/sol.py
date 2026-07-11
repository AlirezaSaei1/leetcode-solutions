class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        while i < len(nums):
            start = nums[i]
            j = i + 1
            while j < len(nums) and nums[j] == nums[j-1] + 1:
               j += 1
            end = nums[j-1]
            
            if start == end:
                result.append(f'{start}')
            else:
                result.append(f'{start}->{end}')
            i = j
        
        return result

