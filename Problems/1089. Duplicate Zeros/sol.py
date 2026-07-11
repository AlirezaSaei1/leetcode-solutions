class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = zeros = arr.count(0)
        n = len(arr)
        i = n - 1
        j = n - 1 + zeros 
                    
        while i < j:
            if arr[i] != 0:
                if j < n:
                    arr[j] = arr[i]
            else:
                if j < n:
                    arr[j] = 0
                j -= 1
                if j < n:
                    arr[j] = 0
            i -= 1
            j -= 1


        