class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        size = len(original)
        result = []
        elems = 0

        if m * n != size:
            return result
        
        while elems != m*n:
            result.append(original[elems:elems+n])
            elems += n
        
        return result