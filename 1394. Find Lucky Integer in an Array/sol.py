class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        largest = 0
        for key in count:
            if count[key] == key:
                if key > largest:
                    largest = key
        
        return largest if largest != 0 else -1