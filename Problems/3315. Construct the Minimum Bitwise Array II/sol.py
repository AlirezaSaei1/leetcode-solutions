class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for p in nums:
            if p == 2:
                ans.append(-1)
                continue

            t = 0
            while (p & (1 << t)) != 0:
                t += 1

            ans.append(p - (1 << (t - 1)))

        return ans
