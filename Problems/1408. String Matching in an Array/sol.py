class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = []

        for w1 in words:
            for w2 in words:
                if w2 != w1 and w1 in w2:
                    substrings.append(w1)
                    break
        
        return substrings