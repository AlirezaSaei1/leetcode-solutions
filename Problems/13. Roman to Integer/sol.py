class Solution:
    def romanToInt(self, s: str) -> int:
        rti = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        converted_num = 0
        i = 0
        while i < len(s) - 1:
            if rti[s[i]] < rti[s[i+1]]:
                converted_num += rti[s[i+1]] - rti[s[i]]
                i += 2
            else:
                converted_num += rti[s[i]]
                i += 1

        if i == len(s) - 1:
            converted_num += rti[s[i]]

        return converted_num
