class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        result = []
        for top in words:
            for left in words:
                if left == top:
                    continue
                if left[0] != top[0]:
                    continue
                    
                for right in words:
                    if right in (top, left):
                        continue

                    if right[0] != top[3]:
                        continue
                        
                    for bottom in words:
                        if bottom in (top, left, right):
                            continue

                        if bottom[0] != left[3]:
                            continue

                        if bottom[3] != right[3]:
                            continue
                        
                        result.append([top, left, right, bottom])
        result.sort()
        return result