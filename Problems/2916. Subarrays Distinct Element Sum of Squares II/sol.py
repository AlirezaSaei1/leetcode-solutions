class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        sum_d = [0] * (4 * n)
        sum_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push_down(node: int, l: int, r: int):
            if lazy[node] == 0:
                return

            val = lazy[node]
            mid = (l + r) // 2
            left, right = 2 * node, 2 * node + 1
            len_l, len_r = mid - l + 1, r - mid

            sum_sq[left] = (sum_sq[left] + 2 * val * sum_d[left] + val * val * len_l) % MOD
            sum_d[left] = (sum_d[left] + val * len_l) % MOD
            lazy[left] = (lazy[left] + val) % MOD

            sum_sq[right] = (sum_sq[right] + 2 * val * sum_d[right] + val * val * len_r) % MOD
            sum_d[right] = (sum_d[right] + val * len_r) % MOD
            lazy[right] = (lazy[right] + val) % MOD

            lazy[node] = 0

        def update(node: int, l: int, r: int, ql: int, qr: int, val: int):
            if ql <= l and r <= qr:
                length = r - l + 1
                sum_sq[node] = (sum_sq[node] + 2 * val * sum_d[node] + val * val * length) % MOD
                sum_d[node] = (sum_d[node] + val * length) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return

            push_down(node, l, r)
            mid = (l + r) // 2
            left, right = 2 * node, 2 * node + 1

            if ql <= mid:
                update(left, l, mid, ql, qr, val)
            if qr > mid:
                update(right, mid + 1, r, ql, qr, val)

            sum_d[node] = (sum_d[left] + sum_d[right]) % MOD
            sum_sq[node] = (sum_sq[left] + sum_sq[right]) % MOD

        total_ans = 0
        last_pos = {}

        for i, val in enumerate(nums):
            p = last_pos.get(val, -1)
            update(1, 0, n - 1, p + 1, i, 1)
            last_pos[val] = i
            total_ans = (total_ans + sum_sq[1]) % MOD

        return total_ans