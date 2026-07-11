class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        
        for c in costs:
            freq[c] += 1
            
        count = 0
        for price in range(1, max_cost + 1):
            num_bars = freq[price]
            
            if num_bars > 0:
                if coins >= price * num_bars:
                    coins -= price * num_bars
                    count += num_bars
                else:
                    count += coins // price
                    break
                    
        return count