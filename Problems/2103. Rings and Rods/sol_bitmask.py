class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [0] * 10
        color_map = {'R': 1, 'G': 2, 'B': 4}
        
        for i in range(0, len(rings), 2):
            color_bit = color_map[rings[i]]
            rod_idx = int(rings[i+1])
            rods[rod_idx] |= color_bit
            
        return rods.count(7)