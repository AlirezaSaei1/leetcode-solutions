class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freqs = Counter(arr)
        counter = 0

        for elem in arr:
            if freqs[elem] == 1:
                counter += 1
            
            if counter == k:
                return elem
        
        return ''