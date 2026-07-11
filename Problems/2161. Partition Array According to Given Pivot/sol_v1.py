class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low = []
        eq = 0
        high = []

        for num in nums:
            if num < pivot:
                low.append(num)
            elif num > pivot:
                high.append(num)
            else:
                eq += 1
        
        return low + ([pivot] * eq) + high