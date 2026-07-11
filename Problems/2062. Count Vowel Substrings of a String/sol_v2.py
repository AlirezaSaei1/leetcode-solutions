class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def atMost(k):
            count = 0
            left = 0
            vowel_map = {}
            vowels = set('aeiou')
            
            for right in range(len(word)):
                if word[right] not in vowels:
                    vowel_map.clear()
                    left = right + 1
                    continue
                
                vowel_map[word[right]] = vowel_map.get(word[right], 0) + 1
                
                while len(vowel_map) > k:
                    vowel_map[word[left]] -= 1
                    if vowel_map[word[left]] == 0:
                        del vowel_map[word[left]]
                    left += 1
                
                count += (right - left + 1)
                
            return count

        return atMost(5) - atMost(4)