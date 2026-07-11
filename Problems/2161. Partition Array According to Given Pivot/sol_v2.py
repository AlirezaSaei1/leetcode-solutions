class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = [pivot] * n
        
        left = 0
        right = n - 1
        
        for i in range(n):
            if nums[i] < pivot:
                ans[left] = nums[i]
                left += 1
                
            if nums[n - 1 - i] > pivot:
                ans[right] = nums[n - 1 - i]
                right -= 1
                
        return ans