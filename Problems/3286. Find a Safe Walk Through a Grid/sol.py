class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        start_health = health - grid[0][0]
        if start_health <= 0:
            return False

        max_health_seen = [[-1] * n for _ in range(m)]
        max_health_seen[0][0] = start_health

        q = deque([(0, 0, start_health)])

        while q:
            r, c, cur_health = q.popleft()
        
            if r == m-1 and c == n-1 and cur_health > 0:
                return True
            
            for dirr, dirc in directions:
                new_r = r + dirr
                new_c = c + dirc

                if 0 <= new_r < m and 0 <= new_c < n:
                    next_health = cur_health - grid[new_r][new_c]

                    if next_health > 0 and next_health > max_health_seen[new_r][new_c]:
                        max_health_seen[new_r][new_c] = next_health
                        q.append((new_r, new_c, next_health))
            
        return False