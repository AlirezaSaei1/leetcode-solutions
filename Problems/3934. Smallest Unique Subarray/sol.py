class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MOD1 = 1_000_000_007
        MOD2 = 1_000_000_009
        BASE1 = random.randint(100_005, 1_000_000)
        BASE2 = random.randint(100_005, 1_000_000)

        # Precompute prefix hashes and base powers
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)

        for i, val in enumerate(nums):
            h1[i + 1] = (h1[i] * BASE1 + val) % MOD1
            h2[i + 1] = (h2[i] * BASE2 + val) % MOD2
            p1[i + 1] = (p1[i] * BASE1) % MOD1
            p2[i + 1] = (p2[i] * BASE2) % MOD2

        def has_unique_subarray(length: int) -> bool:
            counts = {}
            pow1 = p1[length]
            pow2 = p2[length]

            for i in range(n - length + 1):
                sub1 = (h1[i + length] - h1[i] * pow1) % MOD1
                sub2 = (h2[i + length] - h2[i] * pow2) % MOD2
                key = (sub1 << 32) | sub2
                counts[key] = counts.get(key, 0) + 1

            return 1 in counts.values()

        lo, hi = 1, n
        ans = n

        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_subarray(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans