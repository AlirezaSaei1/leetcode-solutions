class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = sorted([nums[i] for i in range(0, len(nums), 2)])
        odds = sorted([nums[i] for i in range(1, len(nums), 2)], reverse=True)
        
        for i, val in enumerate(evens):
            nums[i * 2] = val
            
        for i, val in enumerate(odds):
            nums[i * 2 + 1] = val
            
        return nums