class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        cur_len = 0
        n = len(s)

        for i in range(len(words)):
            wlen = len(words[i])
            cur_len += wlen

            if cur_len == n:
                if s == ''.join(words[:i+1]):
                    return True
            
            if cur_len > n:
                break
        
        return False