class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        numr = list(reversed(num))
        kk = list(map(int, reversed(str(k))))
        
        maxlen = max(len(numr), len(kk))
        result = []
        carry = 0
        
        for i in range(maxlen):
            digit_num = numr[i] if i < len(numr) else 0
            digit_k = kk[i] if i < len(kk) else 0
            carry, digit = divmod(digit_num + digit_k + carry, 10)
            result.append(digit)
        
        if carry:
            result.append(carry)
        
        return list(reversed(result))
