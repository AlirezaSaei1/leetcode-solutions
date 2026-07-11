class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
            
        n = len(s)
        dp = [False] * n
        dp[0] = True
        
        reachable_options_in_window = 0
        
        for i in range(1, n):
            # 1. Slide the window forward: Add new elements entering the range
            if i >= minJump and dp[i - minJump]:
                reachable_options_in_window += 1
                
            # 2. Slide the window forward: Remove old elements leaving the range
            if i > maxJump and dp[i - maxJump - 1]:
                reachable_options_in_window -= 1
                
            # 3. If we have at least one reachable option in our window AND s[i] is '0'
            if s[i] == '0' and reachable_options_in_window > 0:
                dp[i] = True
                
        return dp[-1]