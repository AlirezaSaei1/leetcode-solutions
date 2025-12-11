class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0 :
            return [0] * n
        
        arr = code * 2
        pref_arr = [0] * (2 * n + 1)
        for i in range(2 * n):
            pref_arr[i + 1] = pref_arr[i] + arr[i]
        
        result = [0] * n

        if k > 0:
            for i in range(n):
                result[i] = pref_arr[i + k + 1] - pref_arr[i + 1]
        else:
            for i in range(n):
                result[i] = pref_arr[i + n] - pref_arr[i + n + k]
            
        return result
