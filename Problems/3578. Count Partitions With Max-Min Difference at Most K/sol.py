class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        dp = [0] * n
        pref = [0] * n

        maxdq = deque()
        mindq = deque()

        L = 0

        for i in range(n):
            while maxdq and maxdq[-1] < nums[i]:
                maxdq.pop()
            maxdq.append(nums[i])
            
            while mindq and mindq[-1] > nums[i]:
                mindq.pop()
            mindq.append(nums[i])

            while maxdq[0] - mindq[0] > k:
                if maxdq[0] == nums[L]:
                    maxdq.popleft()
                if mindq[0] == nums[L]:
                    mindq.popleft()
                L += 1
            
            if L == 0:
                dp[i] = (1 + (pref[i-1] if i > 0 else 0)) % MOD
            else:
                left_sum = pref[i-1]
                right_sum = pref[L-2] if L >= 2 else 0
                dp[i] = (left_sum - right_sum) % MOD

            pref[i] = (dp[i] + (pref[i-1] if i > 0 else 0)) % MOD

        return dp[-1]
