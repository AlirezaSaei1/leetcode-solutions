class Solution:
    def secondHighest(self, s: str) -> int:
        first, second = -1, -1
        chars = set(list(s))

        for char in chars:
            if char.isnumeric():
                n = int(char)
                if n > first:
                    second = first
                    first = n
                elif n > second:
                    second = n

        return second if second != -1 else -1