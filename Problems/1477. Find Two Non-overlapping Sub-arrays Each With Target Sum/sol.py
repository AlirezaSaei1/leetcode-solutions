class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * n
        
        seen = {0: -1}
        prefix_sum = 0
        ans = float('inf')
        min_len_so_far = float('inf')

        for i in range(n):
            prefix_sum += arr[i]
            seen[prefix_sum] = i
            
            needed = prefix_sum - target
            if needed in seen:
                l = seen[needed]
                curr_len = i - l
                
                if l >= 0 and best[l] != float('inf'):
                    ans = min(ans, curr_len + best[l])

                min_len_so_far = min(min_len_so_far, curr_len)
            
            best[i] = min_len_so_far

        return ans if ans != float('inf') else -1