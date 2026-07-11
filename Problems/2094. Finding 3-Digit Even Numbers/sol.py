class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digit_counts = Counter(digits)
        res = []
        
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            needed = Counter([d1, d2, d3])
            
            possible = True
            for digit, count in needed.items():
                if digit_counts[digit] < count:
                    possible = False
                    break
            
            if possible:
                res.append(num)
                
        return res