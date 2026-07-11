class Solution:
    def countValidWords(self, sentence: str) -> int:
        def valid(token: str) -> bool:
            hyphen = 0
            punctuation = 0
            
            for i, ch in enumerate(token):
                if ch.isdigit():
                    return False
                
                if ch == '-':
                    hyphen += 1
                    if hyphen > 1:
                        return False
                        
                    if i == 0 or i == len(token) - 1:
                        return False
                    if not (token[i - 1].islower() and token[i + 1].islower()):
                        return False
                
                elif ch in "!.,":
                    punctuation += 1
                    if punctuation > 1:
                        return False

                    if i != len(token) - 1:
                        return False
                
                elif not ch.islower():
                    return False
            
            return True
        
        return sum(valid(token) for token in sentence.split())