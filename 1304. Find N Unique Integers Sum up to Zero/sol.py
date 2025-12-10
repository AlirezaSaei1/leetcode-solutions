class Solution:
    def sumZero(self, n: int) -> List[int]:
        m = n // 2
        answer = list(range(-m, m+1))
        
        if n % 2 == 0:
            answer.remove(0)
    
        return answer