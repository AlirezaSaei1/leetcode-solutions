class SegmentTree:
    def __init__(self, arr: list[int], k: int):
        self.n = len(arr)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_counts = [[0] * k for _ in range(4 * self.n)]
        self.build(arr, 0, 0, self.n - 1)

    def _merge(self, tree_idx: int, l_node: int, r_node: int):
        # Merge product modulo k
        l_prod = self.tree_prod[l_node]
        r_prod = self.tree_prod[r_node]
        self.tree_prod[tree_idx] = (l_prod * r_prod) % self.k

        # Combine prefix counts
        counts = list(self.tree_counts[l_node])
        for r_rem in range(self.k):
            r_cnt = self.tree_counts[r_node][r_rem]
            if r_cnt > 0:
                combined_rem = (l_prod * r_rem) % self.k
                counts[combined_rem] += r_cnt
        self.tree_counts[tree_idx] = counts

    def build(self, arr: list[int], node: int, l: int, r: int):
        if l == r:
            val = arr[l] % self.k
            self.tree_prod[node] = val
            self.tree_counts[node][val] = 1
            return

        mid = (l + r) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        self.build(arr, left_child, l, mid)
        self.build(arr, right_child, mid + 1, r)
        self._merge(node, left_child, right_child)

    def update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            v = val % self.k
            self.tree_prod[node] = v
            self.tree_counts[node] = [0] * self.k
            self.tree_counts[node][v] = 1
            return

        mid = (l + r) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        if idx <= mid:
            self.update(left_child, l, mid, idx, val)
        else:
            self.update(right_child, mid + 1, r, idx, val)

        self._merge(node, left_child, right_child)

    def query(self, node: int, l: int, r: int, ql: int, qr: int):
        # Returns (prod, counts) for segment [ql, qr]
        if ql <= l and r <= qr:
            return self.tree_prod[node], self.tree_counts[node]

        mid = (l + r) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        if qr <= mid:
            return self.query(left_child, l, mid, ql, qr)
        if ql > mid:
            return self.query(right_child, mid + 1, r, ql, qr)

        l_prod, l_counts = self.query(left_child, l, mid, ql, qr)
        r_prod, r_counts = self.query(right_child, mid + 1, r, ql, qr)

        combined_prod = (l_prod * r_prod) % self.k
        combined_counts = list(l_counts)
        for r_rem in range(self.k):
            r_cnt = r_counts[r_rem]
            if r_cnt > 0:
                combined_rem = (l_prod * r_rem) % self.k
                combined_counts[combined_rem] += r_cnt

        return combined_prod, combined_counts


class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        st = SegmentTree(nums, k)
        ans = []

        for idx, val, start, x in queries:
            st.update(0, 0, n - 1, idx, val)
            _, counts = st.query(0, 0, n - 1, start, n - 1)
            ans.append(counts[x])

        return ans