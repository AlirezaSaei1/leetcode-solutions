class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(x1 - x2) for x1, x2 in zip(nums1, nums2)]

        max_diff = max(diffs)
        if max_diff == 0 or k == 0:
            return sum(d * d for d in diffs)

        freq = [0] * (max_diff + 1)
        for d in diffs:
            freq[d] += 1

        for d in range(max_diff, 0, -1):
            if freq[d] == 0:
                continue

            if k >= freq[d]:
                k -= freq[d]
                freq[d - 1] += freq[d]
                freq[d] = 0
            else:
                freq[d] -= k
                freq[d - 1] += k
                k = 0
                break

        return sum(d * d * count for d, count in enumerate(freq))