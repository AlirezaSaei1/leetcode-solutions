class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        
        count = [0] * 51
        for c in capacity:
            count[c] += 1
            
        used_boxes = 0
        
        for size in range(50, 0, -1):
            if count[size] > 0:
                needed = (total_apples + size - 1) // size
                
                take = min(count[size], needed)
                
                total_apples -= take * size
                used_boxes += take
                
                if total_apples <= 0:
                    return used_boxes
                    
        return used_boxes