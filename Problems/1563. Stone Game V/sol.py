class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @cache
        def dp(i, j):
            if i == j:
                return 0

            max_score = 0
            for k in range(i, j):
                left_sum = prefix[k + 1] - prefix[i]
                right_sum = prefix[j + 1] - prefix[k + 1]

                if left_sum < right_sum:
                    if max_score >= left_sum * 2:
                        continue
                    max_score = max(max_score, left_sum + dp(i, k))
                elif left_sum > right_sum:
                    if max_score >= right_sum * 2:
                        break
                    max_score = max(max_score, right_sum + dp(k + 1, j))
                else:
                    max_score = max(max_score, left_sum + dp(i, k), right_sum + dp(k + 1, j))

            return max_score

        return dp(0, n - 1)