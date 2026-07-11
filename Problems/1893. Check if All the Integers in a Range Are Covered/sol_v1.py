class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [False] * (right - left + 1)
        
        for start, end in ranges:
            clamped_start = max(start, left)
            clamped_end = min(end, right)
            
            for i in range(clamped_start, clamped_end + 1):
                covered[i - left] = True
        
        return all(covered)