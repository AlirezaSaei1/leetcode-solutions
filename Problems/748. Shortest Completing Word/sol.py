class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        chars = [0] * 26
        
        for char in licensePlate:
            if char.isalpha():
                char = char.lower()
                idx = ord(char) - ord('a')
                chars[idx] += 1
        
        shortest_word = None

        for word in words:
            word_chars = [0] * 26

            for char in word:
                idx = ord(char) - ord('a')
                word_chars[idx] += 1
            
            if all(word_chars[i] >= chars[i] for i in range(26)):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
        
        return shortest_word

