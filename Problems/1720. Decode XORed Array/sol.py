class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        prev = first
        for enc in encoded:
            element = prev ^ enc
            arr.append(element)
            prev = element
        
        return arr