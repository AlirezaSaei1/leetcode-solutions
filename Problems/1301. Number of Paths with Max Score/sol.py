class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        # dp[r][c] = (max_sum, path_count)
        dp = [[(-1, 0) for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = (0, 1)
        
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == 'X' or dp[r][c][0] == -1:
                    continue
                
                curr_sum, curr_count = dp[r][c]
                
                for dr, dc in [(-1, 0), (0, -1), (-1, -1)]:
                    pr, pc = r + dr, c + dc
                    if 0 <= pr < n and 0 <= pc < n and board[pr][pc] != 'X':
                        val = int(board[pr][pc]) if board[pr][pc] != 'E' else 0
                        new_sum = curr_sum + val
                        
                        if new_sum > dp[pr][pc][0]:
                            dp[pr][pc] = (new_sum, curr_count)
                        elif new_sum == dp[pr][pc][0]:
                            dp[pr][pc] = (new_sum, (dp[pr][pc][1] + curr_count) % MOD)
                            
        res = dp[0][0]
        return [res[0], res[1]] if res[0] != -1 else [0, 0]