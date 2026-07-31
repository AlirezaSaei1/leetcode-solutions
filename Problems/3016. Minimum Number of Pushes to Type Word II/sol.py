class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        keys = sorted(freq, key=freq.get, reverse=True)

        pushes = 0
        counter = 0
        amt = 1

        for key in keys:
            if key in ['*', '#'] or key.isdigit():
                pushes += 1
            else:
                pushes += (amt * freq[key])
                counter += 1

            if counter == 8:
                counter = 0 
                amt += 1 
        
        return pushes