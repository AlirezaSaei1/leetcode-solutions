class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0 :
            return [0] * n
        
        decoded = []
        if k > 0:
            full_code = code + code[:k]
            for i in range(n):
                summ = sum(full_code[i+1:i+k+1])
                decoded.append(summ)
        else:
            full_code = code[k:] + code
            for i in range(n):
                summ = sum(full_code[i:i-k])
                decoded.append(summ)
            
        return decoded


