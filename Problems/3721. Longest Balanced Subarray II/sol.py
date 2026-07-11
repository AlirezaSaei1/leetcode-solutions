import sys

sys.setrecursionlimit(200000)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        nxt = [n] * n
        pos = {}

        for i in range(n - 1, -1, -1):
            if nums[i] in pos:
                nxt[i] = pos[nums[i]]
            pos[nums[i]] = i

        self.mn = [0] * (4 * n)
        self.mx = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

        def push(node):
            if self.lazy[node] != 0:
                lz = self.lazy[node]
                self.lazy[2 * node] += lz
                self.mn[2 * node] += lz
                self.mx[2 * node] += lz
                self.lazy[2 * node + 1] += lz
                self.mn[2 * node + 1] += lz
                self.mx[2 * node + 1] += lz
                self.lazy[node] = 0

        def update(node, start, end, L, R, val):
            if L > end or R < start:
                return
            if L <= start and end <= R:
                self.mn[node] += val
                self.mx[node] += val
                self.lazy[node] += val
                return
            
            push(node)
            mid = (start + end) // 2
            update(2 * node, start, mid, L, R, val)
            update(2 * node + 1, mid + 1, end, L, R, val)
            self.mn[node] = min(self.mn[2 * node], self.mn[2 * node + 1])
            self.mx[node] = max(self.mx[2 * node], self.mx[2 * node + 1])

        def query(node, start, end, L, R):
            if L > end or R < start or self.mn[node] > 0 or self.mx[node] < 0:
                return -1
            
            if start == end:
                return start if self.mn[node] == 0 else -1
            
            push(node)
            mid = (start + end) // 2
            
            res = query(2 * node + 1, mid + 1, end, L, R)
            if res != -1:
                return res
            return query(2 * node, start, mid, L, R)

        for val, idx in pos.items():
            sign = 1 if val % 2 != 0 else -1
            update(1, 0, n - 1, idx, n - 1, sign)

        ans = 0
        
        for l in range(n):
            last_zero_idx = query(1, 0, n - 1, l, n - 1)
            
            if last_zero_idx != -1:
                ans = max(ans, last_zero_idx - l + 1)
            
            sign = 1 if nums[l] % 2 != 0 else -1
            limit = nxt[l] - 1
            update(1, 0, n - 1, l, limit, -sign)
            
        return ans