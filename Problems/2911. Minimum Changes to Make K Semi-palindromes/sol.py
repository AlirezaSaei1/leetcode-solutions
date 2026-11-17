class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        divisors = [[] for _ in range(n + 1)]
        for d in range(1, n):
            for length in range(2 * d, n + 1, d):
                divisors[length].append(d)
                
        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = float('inf')
                for d in divisors[length]:
                    changes = 0
                    for r in range(d):
                        left = i + r
                        right = j - d + 1 + r
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    if changes < best:
                        best = changes
                cost[i][j] = best
                
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        
        for p in range(1, k + 1):
            for j in range(2 * p, n - 2 * (k - p) + 1):
                for i in range(2 * (p - 1), j - 1):
                    if dp[p - 1][i] + cost[i][j - 1] < dp[p][j]:
                        dp[p][j] = dp[p - 1][i] + cost[i][j - 1]
                        
        return dp[k][n]