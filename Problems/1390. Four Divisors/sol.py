class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def four_divisors_sum(num):
            divs = set()
            for i in range(1, int(sqrt(num)) + 1):
                if num % i == 0:
                    divs.add(i)
                    divs.add(num // i)
                
                if len(divs) > 4:
                    return 0
                
            return sum(divs) if len(divs) == 4 else 0

        answer = 0
        for num in nums:
            answer += four_divisors_sum(num)
        
        return answer