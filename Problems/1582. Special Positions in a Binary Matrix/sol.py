class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        rows = [sum(r) for r in mat]
        cols = [0] * m

        for i in range(n):
            row = mat[i]
            for j in range(m):
                cols[j] += row[j]

        count = 0

        for i in range(n):
            if rows[i] == 1:
                j = mat[i].index(1)
                if cols[j] == 1:
                    count += 1

        return count
