class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        val_set = set()
        for v in counter.values():
            if v in val_set:
                return False
            else:
                val_set.add(v)
        
        return True