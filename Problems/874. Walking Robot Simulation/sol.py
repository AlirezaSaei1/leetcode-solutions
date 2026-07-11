class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        x, y = 0, 0
        di = 0 
        
        obstacle_set = set(map(tuple, obstacles))
        max_dist_sq = 0
        
        for cmd in commands:
            if cmd == -2:
                di = (di - 1) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    nx = x + dx[di]
                    ny = y + dy[di]
                    
                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
                    max_dist_sq = max(max_dist_sq, x*x + y*y)

        return max_dist_sq