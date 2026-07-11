class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
            
        n = len(s)
        queue = deque([0])
        furthest_reached = 0
        
        while queue:
            idx = queue.popleft()
            
            if idx == n - 1:
                return True
                
            start = max(idx + minJump, furthest_reached + 1)
            end = min(idx + maxJump, n - 1)
            
            for next_idx in range(start, end + 1):
                if s[next_idx] == '0':
                    queue.append(next_idx)

            furthest_reached = max(furthest_reached, end)
            
        return False