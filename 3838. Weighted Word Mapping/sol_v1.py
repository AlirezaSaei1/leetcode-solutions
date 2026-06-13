class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        answer = []
        
        for word in words:
            weight = sum([weights[ord(char) - ord('a')] for char in word])
            weight %= 26
            answer.append(chr(ord('z') - weight))
        
        return ''.join(answer)