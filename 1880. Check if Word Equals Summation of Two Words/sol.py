class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def number(s):
            nums = []
            for char in s:
                nums.append(ord(char) - ord('a'))

            return int("".join(map(str, nums)))
        
        return number(firstWord) + number(secondWord) == number(targetWord)