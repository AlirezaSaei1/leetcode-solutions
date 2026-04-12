class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        indices = [ord(c) - ord('A') for c in word]
        
        def get_dist(p1, p2):
            if p1 == 26 or p2 == 26: return 0
            return abs(p1 // 6 - p2 // 6) + abs(p1 % 6 - p2 % 6)

        # dp[char_idx][finger1_pos][finger2_pos]
        # Size: (n) x (27) x (27)
        dp = [[[float('inf')] * 27 for _ in range(27)] for _ in range(n + 1)]
        
        dp[0][26][26] = 0
        
        for k in range(n):
            target = indices[k]
            for f1 in range(27):
                for f2 in range(27):
                    if dp[k][f1][f2] == float('inf'):
                        continue
                    
                    current_cost = dp[k][f1][f2]
                    
                    # Option 1: Move Finger 1 to the target character
                    cost1 = current_cost + get_dist(f1, target)
                    dp[k+1][target][f2] = min(dp[k+1][target][f2], cost1)
                    
                    # Option 2: Move Finger 2 to the target character
                    cost2 = current_cost + get_dist(f2, target)
                    dp[k+1][f1][target] = min(dp[k+1][f1][target], cost2)
        
        res = float('inf')
        for f1 in range(27):
            for f2 in range(27):
                res = min(res, dp[n][f1][f2])
        return res