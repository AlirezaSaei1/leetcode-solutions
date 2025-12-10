class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 1

        for num in arr:
            if num % 2 == 1:
                count += 1
            else:
                count = 1
            
            if count == 4:
                return True
        else:
            return False