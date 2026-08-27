class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        counts = Counter(s)
        n = len(s)
        
        L = 0
        for i in range(n):
            if counts[target[i]] > 0:
                counts[target[i]] -= 1
                L += 1
            else:
                break
                
        i = L
        while i > min(L, n - 1):
            i -= 1
            counts[target[i]] += 1
            
        for i in range(min(L, n - 1), -1, -1):
            best_c = None

            for c_ord in range(ord(target[i]) + 1, ord('z') + 1):
                c = chr(c_ord)
                if counts[c] > 0:
                    best_c = c
                    break
                    
            if best_c:
                counts[best_c] -= 1
                res = [target[:i], best_c]
                
                for c_ord in range(ord('a'), ord('z') + 1):
                    c = chr(c_ord)
                    if counts[c] > 0:
                        res.append(c * counts[c])
                        
                return "".join(res)

            if i > 0:
                counts[target[i - 1]] += 1
                
        return ""