class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prev = nums[0]
        pref_sum = nums[0]

        for i in range(1, len(nums)):
            if prev + 1 == nums[i]:
                pref_sum += nums[i]
                prev = nums[i]
            else:
                break
        
        st = set(nums)
        while pref_sum in st:
            pref_sum += 1
        
        return pref_sum