class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # m, n = len(mat), len(mat[0])
        # r_i, c_i = 0, 0
        # mat_reshaped = [[0] * c for i in range(r)]

        # if m * n != r * c:
        #     return mat
        # else:
        #     for row in mat:
        #         for entry in row:
        #             if c_i == c:
        #                 r_i += 1
        #                 c_i = 0
        #             mat_reshaped[r_i][c_i] = entry
        #             c_i += 1
        
        # return mat_reshaped
        flat = [num for row in mat for num in row]
        
        if len(flat) != r * c:
            return mat

        return [flat[i * c:(i + 1) * c] for i in range(r)]
                    