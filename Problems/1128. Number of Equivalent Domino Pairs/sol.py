class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = {}
        pairs = 0

        for a, b in dominoes:
            key = 10 * min(a, b) + max(a, b)
            if key in counts:
                pairs += counts[key]
                counts[key] += 1
            else:
                counts[key] = 1

        return pairs
