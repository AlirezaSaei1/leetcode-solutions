class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = sorted([x * x for x in nums])
        
        n = len(nums)
        num_negs = n // 2
        
        return sum(squares[num_negs:]) - sum(squares[:num_negs])