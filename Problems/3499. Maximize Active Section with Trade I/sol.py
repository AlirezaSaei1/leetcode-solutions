class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count('1')
        max_gain = 0

        zero_lengths = []
        n = len(s)
        i = 0
        
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                zero_lengths.append((i, j - i))
                i = j
            else:
                i += 1
                
        if len(zero_lengths) < 2:
            return total_ones
            
        for k in range(len(zero_lengths) - 1):
            end_prev_zero = zero_lengths[k][0] + zero_lengths[k][1]
            start_next_zero = zero_lengths[k+1][0]
            
            if start_next_zero > end_prev_zero:
                gain = zero_lengths[k][1] + zero_lengths[k+1][1]
                max_gain = max(max_gain, gain)
                
        return total_ones + max_gain