class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def optimize_order(start1, dur1, start2, dur2):
            min_finish1 = float('inf')
            for s, d in zip(start1, dur1):
                if s + d < min_finish1:
                    min_finish1 = s + d
            
            best_total_finish = float('inf')
            
            for s2, d2 in zip(start2, dur2):
                start_time_2 = max(min_finish1, s2)
                total_finish = start_time_2 + d2
                
                if total_finish < best_total_finish:
                    best_total_finish = total_finish
                    
            return best_total_finish

        order1 = optimize_order(landStartTime, landDuration, waterStartTime, waterDuration)
        order2 = optimize_order(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(order1, order2)