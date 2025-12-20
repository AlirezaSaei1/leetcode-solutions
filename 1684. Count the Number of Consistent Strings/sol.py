class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        answer = 0
        for word in words:
            for char in word:
                if char not in allowed_set:
                    break
            else:
                answer +=1
        
        return answer