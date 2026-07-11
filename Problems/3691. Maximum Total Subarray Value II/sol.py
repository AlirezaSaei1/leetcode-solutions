class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
            
        # 1. Build Sparse Tables for O(1) Range Queries
        log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            log_table[i] = log_table[i // 2] + 1
            
        max_power = log_table[n] + 1
        st_max = [[0] * max_power for _ in range(n)]
        st_min = [[0] * max_power for _ in range(n)]
        
        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]
            
        for j in range(1, max_power):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j - 1], st_max[i + (1 << (j - 1))][j - 1])
                st_min[i][j] = min(st_min[i][j - 1], st_min[i + (1 << (j - 1))][j - 1])
                
        def query_val(l, r):
            if l > r:
                return 0
            j = log_table[r - l + 1]
            mx = max(st_max[l][j], st_max[r - (1 << j) + 1][j])
            mn = min(st_min[l][j], st_min[r - (1 << j) + 1][j])
            return mx - mn

        # 2. Max-Heap Initialization
        heap = []
        for l in range(n):
            val = query_val(l, n - 1)
            heapq.heappush(heap, (-val, l, n - 1))
            
        total_value = 0
        
        # 3. Process the top K elements lazily
        for _ in range(k):
            if not heap:
                break
                
            neg_val, l, r = heapq.heappop(heap)
            total_value += (-neg_val)

            if r > l:
                next_r = r - 1
                next_val = query_val(l, next_r)
                heapq.heappush(heap, (-next_val, l, next_r))
                
        return total_value