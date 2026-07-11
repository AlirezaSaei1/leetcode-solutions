class Solution:
    def countValidWords(self, sentence: str) -> int:
        tokens = sentence.split()
        pattern = r'^[a-z]+(-[a-z]+)?[!.,]?$|^[!.,]$'
        count = 0

        for token in tokens:
            if re.fullmatch(pattern, token):
                count += 1
        
        return count