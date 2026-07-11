class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest, alt = 0, 0
        for g in gain:
            alt += g
            highest = max(highest, alt)
        
        return highest