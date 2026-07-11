class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_length = 0

        for word in words:
            word_count = {}
            valid = True
            for c in word:
                word_count[c] = word_count.get(c, 0) + 1
                if word_count[c] > chars_count.get(c, 0):
                    valid = False
                    break
            if valid:
                total_length += len(word)

        return total_length