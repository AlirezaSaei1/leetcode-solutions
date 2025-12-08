class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        total_dist = sum(distance)
        clockwise_dist = 0
        
        while start != destination:
            clockwise_dist += distance[start]
            start = (start + 1) % n 
        
        return min(clockwise_dist, total_dist - clockwise_dist)
