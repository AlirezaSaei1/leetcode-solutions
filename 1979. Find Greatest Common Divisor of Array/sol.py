class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn, mx = float('inf'), float('-inf')
        for num in nums:
            if num < mn:
                mn = num
            
            if num > mx:
                mx = num
        
        for i in range(mn, 0, -1):
            if mn % i == 0 and mx % i == 0:
                return i
        else:
            return 1
