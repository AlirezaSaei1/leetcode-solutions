class Solution:
    def canAliceWin(self, n: int) -> bool:
        winner = False
        step = 10

        while n >= step:
            n -= step
            step -= 1
            winner = not winner
        
        return winner