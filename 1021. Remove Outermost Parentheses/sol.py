class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        start = 0
        parts = []
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append('(')
            else:
                stack.pop()
            
            if not stack:
                parts.append(s[start+1:i])
                start = i + 1
        
        return "".join(parts)
