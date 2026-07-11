class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        dp = [1] * m
        
        for i in range(m):
            for j in range(i):
                is_compatible = True
                for k in range(n):
                    if strs[k][j] > strs[k][i]:
                        is_compatible = False
                        break

                if is_compatible:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        max_kept = max(dp) if m > 0 else 0
        return m - max_kept