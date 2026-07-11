class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split()
        prev = -1

        for word in words:
            if word.isnumeric():
                n = int(word)
                if prev < n:
                    prev = n
                else:
                    return False
        
        return True