class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        new_nums = sorted(range(n), key=lambda i: nums[i])
        sorted_vals = [nums[i] for i in new_nums]
        
        get_i = [0] * n
        for rank, original_idx in enumerate(new_nums):
            get_i[original_idx] = rank
            
        st = [[0] * 18 for _ in range(n)]
        r = 0
        for i in range(n):
            if r < i: r = i
            while r + 1 < n and sorted_vals[r + 1] - sorted_vals[r] <= maxDiff and sorted_vals[r + 1] - sorted_vals[i] <= maxDiff:
                r += 1
            st[i][0] = r
            
        for j in range(1, 18):
            for i in range(n):
                st[i][j] = st[st[i][j - 1]][j - 1]
                
        ans = []
        for u, v in queries:
            a, b = get_i[u], get_i[v]
            if a > b: a, b = b, a
            if a == b:
                ans.append(0)
                continue
                
            curr = a
            steps = 0
            for j in range(17, -1, -1):
                if st[curr][j] < b:
                    curr = st[curr][j]
                    steps += (1 << j)
            
            if st[curr][0] >= b:
                ans.append(steps + 1)
            else:
                ans.append(-1)
                
        return ans