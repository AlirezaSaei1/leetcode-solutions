class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'AEIOUaeiou'
        s = list(s)
        start_idx = 0
        end_idx = len(s) - 1

        while start_idx < end_idx:
            while start_idx < end_idx and s[start_idx] not in vowels:
                start_idx += 1
            while start_idx < end_idx and s[end_idx] not in vowels:
                end_idx -= 1
            if start_idx < end_idx:
                s[start_idx], s[end_idx] = s[end_idx], s[start_idx]
                start_idx += 1
                end_idx -= 1

        return ''.join(s)
