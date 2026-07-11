class Solution:
    def countTriples(self, n: int) -> int:
        mem = set()
        for i in range(1, n+1):
            for j in range(1, n+1):
                c = sqrt(i * i + j * j)
                if c <= n and int(c) == c:
                    mem.add((i, j, c))
        
        return len(mem)