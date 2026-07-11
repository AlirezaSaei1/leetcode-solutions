class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        morsed = set()
        for word in words:
            code = ''
            for char in word:
                code += morse[ord(char) - ord('a')]
            morsed.add(code)
        
        return len(morsed)