class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = max(f for f, _ in items)
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1

        div_count = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            for mult in range(f, max_f + 1, f):
                div_count[f] += freq[mult]

        dp = [0] * (budget + 1)

        for f, p in items:
            if p <= budget:
                val = div_count[f]
                for b in range(budget, p - 1, -1):
                    if dp[b - p] + val > dp[b]:
                        dp[b] = dp[b - p] + val

        for p in {p for _, p in items}:
            for b in range(p, budget + 1):
                if dp[b - p] + 1 > dp[b]:
                    dp[b] = dp[b - p] + 1

        return dp[budget]