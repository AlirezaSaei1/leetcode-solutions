class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(points)
        
        slope_to_line = defaultdict(list)
        mid_to_slope = defaultdict(list)
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                
                if dx == 0:
                    sdy, sdx = 1, 0
                else:
                    g = gcd(dy, dx)
                    dy //= g
                    dx //= g

                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    sdy, sdx = dy, dx
                
                c = sdy * x1 - sdx * y1
                slope_to_line[(sdy, sdx)].append(c)
                
                mid = (x1 + x2, y1 + y2)
                mid_to_slope[mid].append((sdy, sdx))
        
        ans = 0
        
        for line_list in slope_to_line.values():
            if len(line_list) <= 1:
                continue
            
            line_count = defaultdict(int)
            for c in line_list:
                line_count[c] += 1
            
            total_sum = 0
            for cnt in line_count.values():
                ans = (ans + total_sum * cnt) % MOD
                total_sum += cnt
        
        for slope_list in mid_to_slope.values():
            if len(slope_list) <= 1:
                continue
            
            slope_count = defaultdict(int)
            for s in slope_list:
                slope_count[s] += 1

            total_sum = 0
            for cnt in slope_count.values():
                ans = (ans - total_sum * cnt) % MOD
                total_sum += cnt
        
        ans %= MOD
        return ans
