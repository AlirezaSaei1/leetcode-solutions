class Solution:
    def countAsterisks(self, s: str) -> int:
        inside_bars = False
        count = 0

        for char in s:
            if char == '|':
                inside_bars = not inside_bars
            elif char == '*' and not inside_bars:
                count += 1

        return count