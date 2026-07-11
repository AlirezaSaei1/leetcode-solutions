class Solution:
    def binaryGap(self, n: int) -> int:
        bin_n = bin(n)[2:]
        
        prev = -1
        max_dist = 0
        
        for i, bit in enumerate(bin_n):
            if bit == "1":
                if prev != -1:
                    max_dist = max(max_dist, i - prev)
                prev = i
                
        return max_dist
