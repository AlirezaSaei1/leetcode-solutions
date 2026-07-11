class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        chars = set(s)
        char_sums = []
        for char in chars:
            char_sums.append(sum(cost[i] for i in range(n) if s[i] == char))

        return sum(cost) - (max(char_sums) if char_sums else 0)