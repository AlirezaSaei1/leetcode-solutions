class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = {}
        used_t_chars = set()

        for i in range(len(s)):
            if not s[i] in mappings:
                if t[i] in used_t_chars:
                    return False
                mappings[s[i]] = t[i]
                used_t_chars.add(t[i])
            else:
                if not mappings[s[i]] == t[i]:
                    return False
            
        return True