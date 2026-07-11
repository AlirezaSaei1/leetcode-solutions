class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        def dnc(i, j, cost):
            if j == i:
                return cost
            
            if nums[i] * k < nums[j]:
                return min(dnc(i+1, j, cost+1), dnc(i, j-1, cost+1))
            else:
                return cost
        
        nums.sort()
        n = len(nums)

        return dnc(0, n-1, 0)
        
