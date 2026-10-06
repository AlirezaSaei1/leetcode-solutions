class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        unmatched_closing = 0

        for char in s:
            if char == '(':
                stack.append('(')
            else:
                if stack:
                    stack.pop()
                else:
                    unmatched_closing += 1
        
        return unmatched_closing + len(stack)