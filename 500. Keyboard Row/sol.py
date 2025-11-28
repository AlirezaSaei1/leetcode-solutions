class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_map = {}
        for c in "qwertyuiop":
            row_map[c] = 1
        for c in "asdfghjkl":
            row_map[c] = 2
        for c in "zxcvbnm":
            row_map[c] = 3

        result = []
        for word in words:
            lower_word = word.lower()
            first_row = row_map[lower_word[0]]
            if all(row_map[c] == first_row for c in lower_word):
                result.append(word)

        return result
