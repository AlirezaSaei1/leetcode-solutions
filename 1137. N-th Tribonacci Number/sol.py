class Solution:
    def tribonacci(self, n: int) -> int:
        curr = 2
        prev3, prev2, prev1 = 0, 1, 1

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            while curr != n:
                new = prev3 + prev2 + prev1
                prev3, prev2, prev1 = prev2, prev1, new  
                curr += 1
        
        return new
