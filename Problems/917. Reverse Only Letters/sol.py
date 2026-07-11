class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        start, end = 0, len(s) - 1

        while start < end:
            if not s[start].isalpha():
                start += 1
            elif not s[end].isalpha():
                end -= 1
            else:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        return "".join(s)
            
            