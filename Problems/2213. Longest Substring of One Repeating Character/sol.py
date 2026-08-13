class Node:
    def __init__(self):
        self.lc = ''
        self.rc = ''
        self.size = 0
        self.mx = 0
        self.lmx = 0
        self.rmx = 0

class SegmentTree:
    def __init__(self, s: str):
        n = len(s)
        self.tr = [Node() for _ in range(4 * n)]
        self._build(1, 0, n - 1, s)

    def _pushup(self, root: Node, left: Node, right: Node):
        root.lc = left.lc
        root.rc = right.rc
        root.size = left.size + right.size
        root.mx = max(left.mx, right.mx)
        root.lmx = left.lmx
        root.rmx = right.rmx
        
        if left.rc == right.lc:
            if left.lmx == left.size:
                root.lmx += right.lmx
            if right.rmx == right.size:
                root.rmx += left.rmx
            root.mx = max(root.mx, left.rmx + right.lmx)

    def _build(self, u: int, l: int, r: int, s: str):
        if l == r:
            self.tr[u].lc = s[l]
            self.tr[u].rc = s[l]
            self.tr[u].size = 1
            self.tr[u].mx = 1
            self.tr[u].lmx = 1
            self.tr[u].rmx = 1
            return
        mid = (l + r) // 2
        self._build(u << 1, l, mid, s)
        self._build(u << 1 | 1, mid + 1, r, s)
        self._pushup(self.tr[u], self.tr[u << 1], self.tr[u << 1 | 1])

    def update(self, u: int, l: int, r: int, p: int, c: str):
        if l == r:
            self.tr[u].lc = c
            self.tr[u].rc = c
            return
        mid = (l + r) // 2
        if p <= mid:
            self.update(u << 1, l, mid, p, c)
        else:
            self.update(u << 1 | 1, mid + 1, r, p, c)
        self._pushup(self.tr[u], self.tr[u << 1], self.tr[u << 1 | 1])

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        tree = SegmentTree(s)
        ans = []
        n = len(s)
        for c, idx in zip(queryCharacters, queryIndices):
            tree.update(1, 0, n - 1, idx, c)
            ans.append(tree.tr[1].mx)
        return ans