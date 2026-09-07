class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        last_added = [0] * 26
        current_total = 1  # Base case

        for char in s:
            char_idx = ord(char) - ord('a')
            
            new_subseqs = current_total
            current_total = (current_total * 2 - last_added[char_idx]) % MOD
            last_added[char_idx] = new_subseqs

        return (current_total - 1 + MOD) % MOD