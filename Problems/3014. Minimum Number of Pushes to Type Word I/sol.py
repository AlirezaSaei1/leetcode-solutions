class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        counter = 0
        amt = 1

        for char in word:
            if char in ['*', '#'] or char.isdigit():
                pushes += 1
            else:
                pushes += amt
                counter += 1

            if counter == 8:
                counter = 0 
                amt += 1 
        
        return pushes