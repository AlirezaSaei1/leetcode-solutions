class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0, 0, 0]
        for stone in stones:
            count[stone % 3] += 1
            
        # Case 1: The count of elements divisible by 3 is even
        if count[0] % 2 == 0:
            return min(count[1], count[2]) > 0
        
        # Case 2: The count of elements divisible by 3 is odd
        return abs(count[1] - count[2]) > 2