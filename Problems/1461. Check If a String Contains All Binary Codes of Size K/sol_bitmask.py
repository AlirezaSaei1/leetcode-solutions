class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        need = 1 << k
        if n < k:
            return False

        seen = [False] * need
        mask = need - 1
        x = 0
        count = 0

        for i, ch in enumerate(s):
            x = ((x << 1) & mask) | (ch == '1')

            if i >= k - 1:
                if not seen[x]:
                    seen[x] = True
                    count += 1
                    if count == need:
                        return True

        return False