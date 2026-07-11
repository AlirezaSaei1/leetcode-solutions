class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        first_elem = {}
        for p in pieces:
            first_elem[p[0]] = p
        
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] in first_elem:
                piece = first_elem[arr[i]]
                for p in piece:
                    if arr[i] == p:
                        i += 1
                    else:
                        return False
            else:
                return False
        else:
            return True