class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        size = 2 * m
        
        T = [[0] * size for _ in range(size)]
        for i in range(m):
            for j in range(m + i + 1, size):
                T[i][j] = 1
        for i in range(m, size):
            for j in range(i - m):
                T[i][j] = 1
                
        def mat_mul(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                row_A = A[i]
                for k in range(size):
                    if row_A[k] == 0: continue
                    row_B = B[k]
                    val_A = row_A[k]
                    for j in range(size):
                        C[i][j] = (C[i][j] + val_A * row_B[j]) % MOD
            return C

        def mat_pow(A, p):
            res = [[0] * size for _ in range(size)]
            for i in range(size): res[i][i] = 1
            while p > 0:
                if p % 2 == 1: res = mat_mul(res, A)
                A = mat_mul(A, A)
                p //= 2
            return res
            
        if n == 1:
            return m
            
        T_res = mat_pow(T, n - 1)
        
        ans = 0
        for i in range(size):
            for j in range(size):
                ans = (ans + T_res[i][j]) % MOD
                
        return ans