class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        ns = len(start)
        goal = bin(goal)[2:]
        ng = len(goal)

        if ns > ng:
           goal = goal.rjust(ns, '0')
        
        if ng > ns:
            start = start.rjust(ng, '0')
        
        return sum([1 for char1, char2 in zip(start, goal) if char1 != char2])