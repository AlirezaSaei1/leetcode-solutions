class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        words = re.findall(r'[a-zA-Z]+', paragraph.lower())
        
        count = {}
        max_word, max_count = None, 0
        
        for word in words:
            if word not in banned_set:
                count[word] = count.get(word, 0) + 1
                if count[word] > max_count:
                    max_word, max_count = word, count[word]
        
        return max_word