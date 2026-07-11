class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda p: p[0])

        maxx = 0
        for i in range(1, len(sorted_points)):
            diff = sorted_points[i][0] - sorted_points[i-1][0]
            if diff > maxx:
                maxx = diff
        
        return maxx