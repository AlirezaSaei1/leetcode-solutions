class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = []

        for i in range(1950, 2051):
            alive = 0
            for log in logs:
                if log[0] <= i and i < log[1]:
                    alive += 1
                
            population.append(alive)
        
        return population.index(max(population)) + 1950
            
            
