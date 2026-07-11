class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        i = 0
        
        while True:
            if words[(startIndex + i) % n] == target:
                return i
            elif words[(startIndex - i) % n] == target:
                return i
            else:
                i += 1
            
            if i > n // 2:
                break
        
        return -1