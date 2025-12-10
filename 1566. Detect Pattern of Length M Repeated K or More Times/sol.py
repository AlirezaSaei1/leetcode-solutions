class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)

        if m * k > n:
            return False
        
        
        for i in range(n - m * k + 1):
            pattern = arr[i:i+m]
            idx = i
            counter = 0
            while idx < n and pattern == arr[idx:idx+m]:
                idx += m
                counter += 1
            
            if counter >= k:
                return True
        else:
            return False