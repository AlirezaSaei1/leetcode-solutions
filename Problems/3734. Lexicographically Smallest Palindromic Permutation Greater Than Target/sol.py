class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        counts = Counter(s)
        odd_chars = [ch for ch, cnt in counts.items() if cnt % 2 == 1]
        
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        freq = {ch: counts.get(ch, 0) // 2 for ch in "abcdefghijklmnopqrstuvwxyz"}
        m = len(s) // 2
        
        def dfs(idx, is_greater, current_half, current_freq):
            if idx == m:
                half_str = "".join(current_half)
                full = half_str + mid_char + half_str[::-1]

                if full > target:
                    return full
                return ""

            if is_greater:
                rem = []
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    rem.extend([ch] * current_freq[ch])
                
                half_str = "".join(current_half) + "".join(rem)
                full = half_str + mid_char + half_str[::-1]
                return full
            
            target_char = target[idx]

            if current_freq[target_char] > 0:
                current_freq[target_char] -= 1
                current_half.append(target_char)
                
                res = dfs(idx + 1, False, current_half, current_freq)
                if res: return res
                
                current_half.pop()
                current_freq[target_char] += 1
            
            for i in range(ord(target_char) - ord('a') + 1, 26):
                ch = chr(i + ord('a'))
                if current_freq[ch] > 0:
                    current_freq[ch] -= 1
                    current_half.append(ch)
                    
                    res = dfs(idx + 1, True, current_half, current_freq)
                    if res: return res

                    current_half.pop()
                    current_freq[ch] += 1
                    
            return ""

        return dfs(0, False, [], freq)