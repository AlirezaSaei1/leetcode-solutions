class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour if hour < 12 else hour - 12
        angle = abs(hour * 30 - minutes * 5.5)
        return min(360 - angle, angle)