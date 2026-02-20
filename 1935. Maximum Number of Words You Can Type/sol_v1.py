class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        answer = 0

        for word in words:
            for char in brokenLetters:
                if char in word:
                    break
            else:
                answer += 1
        
        return answer