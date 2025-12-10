class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        depth = 0

        for log in logs:
            if '..' in log:
                if depth > 0:
                    depth -= 1
            elif '.' in log:
                pass
            else:
                depth += 1
        
        return depth
