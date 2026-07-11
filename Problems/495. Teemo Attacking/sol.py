class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_duration = 0

        for i in range(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] >= duration:
               total_duration += duration
            else:
                total_duration += min(duration, timeSeries[i+1] - timeSeries[i])
        
        return total_duration + duration