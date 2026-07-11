class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        return min(
            counter['b'] // 1,
            counter['a'] // 1,
            counter['l'] // 2,
            counter['o'] // 2,
            counter['n'] // 1
        )
