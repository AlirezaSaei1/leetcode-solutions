class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_run_length = 0
        curr_run_length = 1
        result = 0
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr_run_length += 1
            else:
                result += min(prev_run_length, curr_run_length)
                prev_run_length = curr_run_length
                curr_run_length = 1
        
        result += min(prev_run_length, curr_run_length)
        return result
