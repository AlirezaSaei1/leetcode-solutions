class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_dist(p1, p2):
            if p1 is None: return 0
            return abs(p1 // 6 - p2 // 6) + abs(p1 % 6 - p2 % 6)

        indices = [ord(c) - ord('A') for c in word]
        dp = {None: 0}
        
        for i in range(len(indices) - 1):
            curr_pos, next_pos = indices[i], indices[i+1]
            new_dp = {}
            for other_pos, val in dp.items():
                # Option 1: Move the finger currently at curr_pos to next_pos
                move_curr = val + get_dist(curr_pos, next_pos)
                new_dp[other_pos] = min(new_dp.get(other_pos, float('inf')), move_curr)
                
                # Option 2: Move the "other" finger to next_pos
                move_other = val + get_dist(other_pos, next_pos)
                new_dp[curr_pos] = min(new_dp.get(curr_pos, float('inf')), move_other)
            dp = new_dp
            
        return min(dp.values())