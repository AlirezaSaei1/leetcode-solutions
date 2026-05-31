class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        for ast in asteroids:
            if mass < ast:
                return False
            mass += ast
            
        return True