class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        char_list = list(word)
        n = len(char_list)
        for i in range(n):
            char = char_list[i]
            if not char.isnumeric():
                char_list[i] = ' '
        
        merged = ''.join(char_list)
        split = merged.split(' ')
        unique = set()

        for s in split:
            if s not in ['', ' ']:
                unique.add(int(s))
        
        return len(unique)