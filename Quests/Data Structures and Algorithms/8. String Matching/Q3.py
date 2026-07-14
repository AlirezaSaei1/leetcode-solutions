class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        times = math.ceil(len(b) / len(a))

        if b in (a * times):
            return times
        
        if b in (a * (times + 1)):
            return times + 1

        return -1