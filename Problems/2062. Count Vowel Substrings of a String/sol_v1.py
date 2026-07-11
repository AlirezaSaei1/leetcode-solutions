class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0
        n = len(word)
        vowels = set('aeiou')
        
        for i in range(n):
            vowel_set = set()
            
            for j in range(i, n):
                if word[j] in vowels:
                    vowel_set.add(word[j])
                    
                    if len(vowel_set) == 5:
                        count += 1
                else:
                    break
        
        return count