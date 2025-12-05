class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = s1.split()
        s2_words = s2.split()
        merged = s1_words + s2_words

        uncommon_words = []

        for word in merged:
            if merged.count(word) == 1:
                uncommon_words.append(word)
        
        return uncommon_words