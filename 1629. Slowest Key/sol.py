class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxx = releaseTimes[0]
        answer = keysPressed[0]
        n = len(releaseTimes)

        for i in range(1, n):
            diff = releaseTimes[i] - releaseTimes[i-1]
            if diff > maxx or (diff == maxx and keysPressed[i] > answer):
                maxx = diff
                answer = keysPressed[i]
        
        return answer