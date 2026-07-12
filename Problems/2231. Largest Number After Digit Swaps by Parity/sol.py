class Solution:
    def largestInteger(self, num: int) -> int:
        odds_idx, odds_val = [], []
        evens_idx, evens_val = [], []
        str_num = str(num)

        for i, char in enumerate(str_num):
            ch_int = int(char)
            if ch_int % 2 == 0:
                evens_idx.append(i)
                evens_val.append(char)
            else:
                odds_idx.append(i)
                odds_val.append(char)
        
        odds_val.sort(reverse=True)
        evens_val.sort(reverse=True)
        result = [0] * len(str_num)

        i = 0
        while i < len(odds_val):
            result[odds_idx[i]] = odds_val[i]
            i += 1

        i = 0
        while i < len(evens_val):
            result[evens_idx[i]] = evens_val[i]
            i += 1
        
        return int(''.join(result))

        
