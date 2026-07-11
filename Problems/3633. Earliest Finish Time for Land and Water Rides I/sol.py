class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        answer = float('inf')
        nland = len(landStartTime)
        nwater = len(waterStartTime)

        for i in range(nland):
            land_ended = landStartTime[i] + landDuration[i]
            for j in range(nwater):
                water_started = max(land_ended, waterStartTime[j])
                answer = min(answer, water_started + waterDuration[j])

        for i in range(nwater):
            water_ended = waterStartTime[i] + waterDuration[i]
            for j in range(nland):
                land_started = max(water_ended, landStartTime[j])
                answer = min(answer, land_started + landDuration[j])
        
        return answer