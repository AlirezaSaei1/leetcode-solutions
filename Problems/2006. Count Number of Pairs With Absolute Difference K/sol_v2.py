class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        ans = 0

        for x in nums:
            ans += freq[x - k] + freq[x + k]
            freq[x] += 1

        return ans