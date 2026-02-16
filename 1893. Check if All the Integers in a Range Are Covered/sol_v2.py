class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for x in range(left, right + 1):
            is_found = False
            for start, end in ranges:
                if start <= x <= end:
                    is_found = True
                    break
                    
            if not is_found:
                return False
                
        return True