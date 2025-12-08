class Solution:
    def countTriples(self, n: int) -> int:
        squares = [i * i for i in range(1, n + 1)]
        
        ans = 0
        for a in range(1, n + 1):
            aa = a * a
            for b in range(1, n + 1):
                s = aa + b * b
                
                idx = bisect_left(squares, s)
                if idx < len(squares) and squares[idx] == s:
                    ans += 1
        
        return ans
