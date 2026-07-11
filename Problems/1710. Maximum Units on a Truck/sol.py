class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total_unit = 0
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        for num, unit in boxTypes:
            if num <= truckSize:
                total_unit += (unit * num)
            else:
                total_unit += (unit * truckSize)
                break
            
            truckSize -= num
        
        return total_unit