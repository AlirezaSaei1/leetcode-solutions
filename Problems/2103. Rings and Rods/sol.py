class Solution:
    def countPoints(self, rings: str) -> int:
        rods = defaultdict(set)

        for i in range(0, len(rings), 2):
            color, rod = rings[i], int(rings[i+1])
            rods[rod].add(color)
        
        return sum([int(len(rods[key]) == 3) for key in rods])
