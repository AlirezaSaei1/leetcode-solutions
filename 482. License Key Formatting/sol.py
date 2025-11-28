class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        
        first_group_len = len(s) % k or k

        parts = [s[:first_group_len]]

        for i in range(first_group_len, len(s), k):
            parts.append(s[i:i+k])

        return '-'.join(parts)
