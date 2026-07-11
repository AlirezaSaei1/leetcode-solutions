class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        ans = 0

        for b in range(n - 3, 0, -1):
            c = b + 1
            for d in range(c + 1, n):
                cnt[nums[d] - nums[c]] += 1

            for a in range(b):
                ans += cnt[nums[a] + nums[b]]

        return ans