class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        total_len = n + m - 1
        res = [None] * total_len
        
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if res[i + j] is not None and res[i + j] != str2[j]:
                        return ""
                    res[i + j] = str2[j]
        
        for i in range(total_len):
            if res[i] is None:
                res[i] = 'a'
        
        fixed = [False] * total_len
        for i in range(n):
            if str1[i] == 'T':
                for j in range(i, i + m):
                    fixed[j] = True

        def get_match(start):
            for i in range(m):
                if res[start + i] != str2[i]:
                    return False
            return True

        for i in range(n):
            if str1[i] == 'F' and get_match(i):
                changed = False
                for j in range(i + m - 1, i - 1, -1):
                    if not fixed[j]:
                        original = res[j]
                        for char_code in range(ord(original) + 1, ord('z') + 1):
                            res[j] = chr(char_code)
                            changed = True
                            break
                        if changed: break
                if not changed: return ""

        for i in range(n):
            match = get_match(i)
            if str1[i] == 'T' and not match: return ""
            if str1[i] == 'F' and match: return ""
            
        return "".join(res)