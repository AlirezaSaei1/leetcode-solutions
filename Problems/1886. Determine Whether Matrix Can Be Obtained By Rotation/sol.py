class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_90_cw(m: List[List[int]]) -> List[List[int]]:
            return [list(row) for row in zip(*m[::-1])]

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate_90_cw(mat)

        return False