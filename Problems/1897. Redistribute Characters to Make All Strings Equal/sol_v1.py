class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        overall_dict = defaultdict(int)

        for word in words:
            for char in word:
                overall_dict[char] += 1
        
        for char in overall_dict:
            if overall_dict[char] % n != 0:
                return False
        
        return True
