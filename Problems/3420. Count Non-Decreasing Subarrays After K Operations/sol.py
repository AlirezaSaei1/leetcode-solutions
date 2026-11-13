class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        ans = 0
        ops = 0
        r = n - 1

        for l in range(n - 1, -1, -1):
            x = nums[l]
            count = 1

            while dq and dq[0][0] <= x:
                val, c = dq.popleft()
                ops += (x - val) * c
                count += c

            dq.appendleft([x, count])

            while ops > k:
                ops -= dq[-1][0] - nums[r]
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                r -= 1

            ans += r - l + 1

        return ans