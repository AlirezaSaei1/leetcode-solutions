class Solution:
    def sortString(self, s: str) -> str:
        count = Counter(s)
        chars = sorted(count.keys())
        result = []

        while len(result) < len(s):
            for c in chars:
                if count[c] > 0:
                    result.append(c)
                    count[c] -= 1

            for c in reversed(chars):
                if count[c] > 0:
                    result.append(c)
                    count[c] -= 1

        return ''.join(result)