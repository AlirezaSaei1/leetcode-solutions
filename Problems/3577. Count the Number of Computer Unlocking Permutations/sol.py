class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        first = complexity[0]
        MOD = 10 ** 9 + 7
        
        for i in range(1, n):
            if complexity[i] <= first:
                return 0
        else:
            return factorial(n - 1) % MOD