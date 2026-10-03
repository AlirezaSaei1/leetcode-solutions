class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                else:
                    prev_idx = i - dp[i - 1] - 1
                    if prev_idx >= 0 and s[prev_idx] == '(':
                        dp[i] = dp[i - 1] + 2 + (dp[prev_idx - 1] if prev_idx >= 1 else 0)

                max_len = max(max_len, dp[i])

        return max_len