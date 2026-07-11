class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = Counter(chain.from_iterable(words))
        n = len(words)
        
        return all(c % n == 0 for c in counts.values())