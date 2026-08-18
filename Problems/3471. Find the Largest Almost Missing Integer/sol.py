class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == n:
            return max(nums)
        
        if k == 1:
            counts = [0] * 51 
            for num in nums:
                counts[num] += 1
                
            for i in range(50, -1, -1):
                if counts[i] == 1:
                    return i
            return -1

        start, end = nums[0], nums[-1]
        if start == end:
            return -1
            
        mx, mn = (start, end) if start > end else (end, start)
        if nums.count(mx) == 1:
            return mx
        if nums.count(mn) == 1:
            return mn
            
        return -1