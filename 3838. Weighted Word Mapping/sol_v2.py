class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        char_weights = [weights[i] for i in range(26)]
        ord_a = ord('a')
        ord_z = ord('z')
        
        answer = []
        for word in words:
            weight = sum(char_weights[ord(char) - ord_a] for char in word) % 26
            answer.append(chr(ord_z - weight))
            
        return ''.join(answer)