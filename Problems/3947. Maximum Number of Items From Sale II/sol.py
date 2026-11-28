class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        p_min = float('inf')

        for f, p in items:
            freq[f] += 1
            if p < p_min:
                p_min = p

        div_count = [0] * (n + 1)
        for f in range(1, n + 1):
            for mult in range(f, n + 1, f):
                div_count[f] += freq[mult]

        batches = []
        limit = 2 * p_min
        for f, p in items:
            gain = div_count[f] - 1
            if gain > 0 and p < limit:
                batches.append((p, gain))

        batches.sort()

        rem = budget
        copies = 0

        for p, gain in batches:
            if rem < p:
                break
            take = min(gain, rem // p)
            copies += 2 * take
            rem -= take * p

        copies += rem // p_min
        
        return copies