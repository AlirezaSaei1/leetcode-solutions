class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        rooms = len(damage)
        score = 0

        for i in range(rooms):
            trial_hp = hp
            for j in range(i, rooms):
                trial_hp -= damage[j]
                if trial_hp >= requirement[j]:
                    score += 1

        return score