class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        ls = 0
        rs = 0
        opens = 0

        for char in moves:
            if char == 'L':
                ls += 1
            elif char == 'R':
                rs += 1
            else:
                opens += 1
        
        return abs(ls - rs) + opens