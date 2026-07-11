class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        up = [1] * m
        down = [1] * m
        
        for _ in range(n - 1):
            new_up = [0] * m
            new_down = [0] * m
            
            total_up = sum(up) % MOD
            total_down = sum(down) % MOD
            
            curr_up = 0
            curr_down = 0
            
            for y in range(m):
                new_up[y] = (total_down - curr_down - down[y] + 2 * MOD) % MOD
                new_down[y] = curr_up
                
                curr_up = (curr_up + up[y]) % MOD
                curr_down = (curr_down + down[y]) % MOD
                
            up = new_up
            down = new_down
            
        return (sum(up) + sum(down)) % MOD