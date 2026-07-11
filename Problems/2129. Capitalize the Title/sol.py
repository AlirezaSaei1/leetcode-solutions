class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        result = [word.lower() if len(word) < 3 else word.title() for word in words]
        
        return ' '.join(result)