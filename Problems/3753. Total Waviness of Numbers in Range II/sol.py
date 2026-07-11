class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve_up_to(limit_num: int) -> int:
            if limit_num < 100:
                return 0
                
            s = str(limit_num)
            n = len(s)
            
            memo = {}
            
            def get_stat(idx, tight, last_d, sec_last_d, is_leading):
                if idx == n:
                    return 1, 0
                    
                state = (idx, tight, last_d, sec_last_d, is_leading)
                if state in memo:
                    return memo[state]
                
                limit = int(s[idx]) if tight else 9
                ways, waves = 0, 0
                
                for d in range(limit + 1):
                    nxt_tight = tight and (d == limit)
                    if is_leading and d == 0:
                        w, wv = get_stat(idx + 1, nxt_tight, 10, 10, True)
                        ways += w
                        waves += wv
                    else:
                        gain = 0
                        if not is_leading and last_d != 10 and sec_last_d != 10:
                            if sec_last_d < last_d > d or sec_last_d > last_d < d:
                                gain = 1
                        w, wv = get_stat(idx + 1, nxt_tight, d, last_d, False)
                        ways += w
                        waves += wv + gain * w
                        
                memo[state] = (ways, waves)
                return ways, waves

            return get_stat(0, True, 10, 10, True)[1]

        return solve_up_to(num2) - solve_up_to(num1 - 1)