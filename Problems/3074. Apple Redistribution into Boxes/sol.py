class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        
        for i, cap in enumerate(capacity):
            total -= cap
            if total <= 0:
                return i + 1
                
        return len(capacity)