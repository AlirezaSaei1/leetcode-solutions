class Solution
    def toGoatLatin(self, sentence str) - str
        words = sentence.split()
        updated_words = []

        for i, word in enumerate(words)
            modified_word = word
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']
                modified_word += 'ma'
            else
                modified_word = modified_word[1] + modified_word[0] + 'ma'
            
            modified_word += 'a'  (i+1)
            updated_words.append(modified_word)
    
        return ' '.join(updated_words)