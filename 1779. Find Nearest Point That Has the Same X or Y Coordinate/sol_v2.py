# LLM Answer

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        best = float('inf')
        ans = -1
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                d = abs(a - x) + abs(b - y)
                if d < best:
                    best = d
                    ans = i
        return ans
