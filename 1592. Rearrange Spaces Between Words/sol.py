class Solution:
    def reorderSpaces(self, text: str) -> str:
        total_spaces = text.count(' ')
        words = text.split()
        n_words = len(words)

        if n_words == 1:
            return words[0] + ' ' * total_spaces
        
        spaces_between = total_spaces // (n_words - 1)
        remaining = total_spaces % (n_words - 1)
        
        return (' ' * spaces_between).join(words) + ' ' * remaining