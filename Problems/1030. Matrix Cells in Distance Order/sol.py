class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        dists = defaultdict(list)

        for i in range(rows):
            for j in range(cols):
                d = abs(i - rCenter) + abs(j - cCenter)
                dists[d].append([i, j])
        
        result = []
        for d in sorted(dists.keys()):
            result.extend(dists[d])
        
        return result
