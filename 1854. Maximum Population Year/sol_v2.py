class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        delta = [0] * 101
        
        for birth, death in logs:
            delta[birth - 1950] += 1
            delta[death - 1950] -= 1
        
        max_population = 0
        current = 0
        answer_year = 1950
        
        for i in range(101):
            current += delta[i]
            if current > max_population:
                max_population = current
                answer_year = 1950 + i
        
        return answer_year
