class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n):
            waves = 0
            digit_list = [int(digit) for digit in str(n)]
            
            for i in range(1, len(digit_list) - 1):
                prev = digit_list[i-1]
                nex = digit_list[i+1]
                cur = digit_list[i]
                if prev < cur > nex or prev > cur < nex:
                    waves += 1
            
            return waves


        answer = 0
        for i in range(num1, num2 + 1):
            answer += waviness(i)
        
        return answer