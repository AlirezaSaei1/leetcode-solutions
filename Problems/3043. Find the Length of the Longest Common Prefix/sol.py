class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10
                
        max_len = 0
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    current_len = len(str(num))
                    if current_len > max_len:
                        max_len = current_len
                    break
                num //= 10
                
        return max_len
