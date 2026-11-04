class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        
        small = []
        large = []
        
        small_sum = 0
        large_sum = 0
        small_sz = 0
        large_sz = 0
        
        in_small = [False] * n 
        costs = [0] * n
        
        def prune_small(current_i):
            while small and small[0][1] <= current_i - x:
                heapq.heappop(small)
                
        def prune_large(current_i):
            while large and large[0][1] <= current_i - x:
                heapq.heappop(large)
                
        for i in range(n):
            if i >= x:
                old_idx = i - x
                if in_small[old_idx]:
                    small_sum -= nums[old_idx]
                    small_sz -= 1
                else:
                    large_sum -= nums[old_idx]
                    large_sz -= 1
                    
            prune_small(i)
            prune_large(i)
            
            if large and nums[i] > large[0][0]:
                heapq.heappush(large, (nums[i], i))
                large_sum += nums[i]
                large_sz += 1
                in_small[i] = False
            else:
                heapq.heappush(small, (-nums[i], i))
                small_sum += nums[i]
                small_sz += 1
                in_small[i] = True
                
            while small_sz > large_sz + 1:
                prune_small(i)
                neg_val, idx = heapq.heappop(small)
                val = -neg_val
                small_sum -= val
                small_sz -= 1
                heapq.heappush(large, (val, idx))
                large_sum += val
                large_sz += 1
                in_small[idx] = False
                
            while small_sz < large_sz:
                prune_large(i)
                val, idx = heapq.heappop(large)
                large_sum -= val
                large_sz -= 1
                heapq.heappush(small, (-val, idx))
                small_sum += val
                small_sz += 1
                in_small[idx] = True
                
            if i >= x - 1:
                prune_small(i)
                if x % 2 == 1:
                    median = -small[0][0]
                    costs[i] = large_sum - small_sum + median
                else:
                    costs[i] = large_sum - small_sum
                    
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        
        for i in range(n + 1):
            dp[0][i] = 0
            
        for c in range(1, k + 1):
            for i in range(c * x, n + 1):
                dp[c][i] = min(dp[c][i - 1], dp[c - 1][i - x] + costs[i - 1])
                
        return int(dp[k][n])