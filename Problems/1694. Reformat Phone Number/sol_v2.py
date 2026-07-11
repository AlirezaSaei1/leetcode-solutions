class Solution:
    def reformatNumber(self, number: str) -> str:
        s = number.replace('-', '').replace(' ', '')
        
        blocks = []
        i = 0
        
        while len(s) - i > 4:
            blocks.append(s[i : i+3])
            i += 3
        
        if len(s) - i == 4:
            blocks.append(s[i : i+2])
            blocks.append(s[i+2 :])
        else:
            blocks.append(s[i :])

        return "-".join(blocks)