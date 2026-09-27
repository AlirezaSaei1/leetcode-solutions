class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        pair = [0] * n

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        res = []
        i = 0
        step = 1

        while i < n:
            if s[i] in '()':
                i = pair[i]
                step = -step
            else:
                res.append(s[i])
            i += step

        return "".join(res)