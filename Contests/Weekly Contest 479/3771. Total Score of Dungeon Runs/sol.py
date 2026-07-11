class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        rooms = len(damage)
        prefix_damages = [damage[0]]
        for i in range(1, rooms):
            prefix_damages.append(prefix_damages[i-1] + damage[i])

        score = 0

        for i in range(rooms - 1, -1, -1):
            find = requirement[i] + prefix_damages[i] - hp
            bin_idx = bisect_left(prefix_damages, find, 0, i)
            score += (i - bin_idx)
            if hp - prefix_damages[i] >= requirement[i]:
                score += 1
            
        return score
            