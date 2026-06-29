class Solution:
    def countEven(self, num: int) -> int:
        def sum_digit(x):
            summ = 0
            while x > 0:
                summ += x % 10
                x //= 10
            
            return summ

        answer = 0
        for i in range(1, num+1):
            if sum_digit(i) % 2 == 0:
                answer += 1
        
        return answer