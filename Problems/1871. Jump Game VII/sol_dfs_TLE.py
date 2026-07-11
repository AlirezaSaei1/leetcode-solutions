class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        def dfs(idx, target):
            if idx == target:
                return True
            
            valids = range(idx + minJump, min(idx + maxJump, target)+1)
            return any(dfs(next_idx, target) for next_idx in valids if s[next_idx] == '0')

        platforms = list(s)
        n = len(platforms)
        return dfs(0, n-1)