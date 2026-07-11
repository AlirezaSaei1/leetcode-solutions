class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        order = sorted(range(len(mat)), key=lambda i: (sum(mat[i]), i))
        return order[:k]
