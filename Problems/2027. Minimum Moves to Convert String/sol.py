class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        sl = list(s)
        
        i = 0
        count = 0
        while i < n:
            if sl[i] == 'X':
                count += 1
                i += 2
            i += 1
        
        return count
            