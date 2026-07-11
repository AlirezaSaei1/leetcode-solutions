class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ans = counts[1] - (1 - counts[1] % 2)
        
        sorted_keys = sorted(counts.keys())
        for x in sorted_keys:
            if x == 1 or counts[x] == 0:
                continue
            
            curr = x
            curr_len = 0
            while counts[curr] >= 2:
                curr_len += 2
                curr = curr * curr
                if curr not in counts:
                    break
            
            if counts[curr] >= 1:
                curr_len += 1
            else:
                curr_len -= 1
                
            ans = max(ans, curr_len)
            
        return ans