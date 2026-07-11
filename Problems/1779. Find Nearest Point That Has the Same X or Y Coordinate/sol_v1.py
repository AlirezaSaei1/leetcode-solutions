class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def man_dist(p):
            return abs(p[0] - x) + abs(p[1] - y)
        
        min_dist = float('inf')
        answer = -1
        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                dist = man_dist(point)
                if dist < min_dist:
                    min_dist = dist
                    answer = i
        
        return answer