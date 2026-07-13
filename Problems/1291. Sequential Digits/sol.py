class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        answer = []
        n_low = len(str(low))
        n_high = len(str(high))

        for n in range(n_low, n_high+1):
            for i in range(1, 10 - n + 1):
                number = int(''.join([f'{i}' for i in range(i, i + n)]))
                
                if low <= number <= high:
                    answer.append(number)
        
        return answer
