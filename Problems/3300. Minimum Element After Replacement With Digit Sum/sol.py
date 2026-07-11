class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sum_digit(n):
            s = 0
            while n > 0:
                s += (n % 10)
                n //= 10
            
            return s
        

        minimum = float('inf')
        for num in nums:
            minimum = min(minimum, sum_digit(num))
        
        return minimum