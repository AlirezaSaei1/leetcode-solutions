class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        distances = [float('inf')] * n

        recent_idx = None
        for i in range(n):
            if s[i] == c:
                recent_idx = i
                distances[i] = 0
            else:
                if recent_idx is not None:
                    distances[i] = abs(i - recent_idx)
        
        for i in range(n-1, -1, -1):
            dist = abs(i - recent_idx)
            if dist < distances[i]:
                distances[i] = dist
            
            if s[i] == c:
                recent_idx = i
        
        return distances