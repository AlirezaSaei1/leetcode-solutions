class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = -float('inf')
        second = -float('inf')
        third = -float('inf')

        for num in nums:
            if num in [first, second, third]:
                continue
            
            if num > first:
                first, second, third = num, first, second
            elif num < first and num > second:
                second, third = num, second
            elif num < second and num > third:
                third = num
            
        
        return third if third != -float('inf') else first