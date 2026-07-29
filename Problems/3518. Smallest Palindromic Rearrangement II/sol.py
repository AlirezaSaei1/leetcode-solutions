class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)
        half_count = [0] * 26
        mid_char = ""
        
        for c in ascii_lowercase:
            v = cnt[c] // 2
            half_count[ord(c) - ord('a')] = v
            if cnt[c] % 2 == 1:
                mid_char = c
                
        half_len = sum(half_count)
        
        def count_arrangements(counts):
            total = sum(counts)
            res = 1
            for freq in counts:
                res *= math.comb(total, freq)
                if res >= 10**6 + 1:
                    return 10**6 + 1
                total -= freq
            return res

        if count_arrangements(half_count) < k:
            return ""
            
        left_half = []
        for _ in range(half_len):
            for i in range(26):
                if half_count[i] == 0:
                    continue
                half_count[i] -= 1
                arrangements = count_arrangements(half_count)
                if arrangements >= k:
                    left_half.append(ascii_lowercase[i])
                    break
                else:
                    k -= arrangements
                    half_count[i] += 1
                    
        ans = "".join(left_half)
        return ans + mid_char + ans[::-1]