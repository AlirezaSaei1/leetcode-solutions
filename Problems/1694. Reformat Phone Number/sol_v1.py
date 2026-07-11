class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-', '').replace(' ', '')
        n = len(number)

        i = 0
        while n - i > 4:
            i += 3
            number = number[:i] + '-' + number[i:]
            n += 1
            i += 1
        
        if n - i == 4:
           number = number[:i+2] + '-' + number[i+2:]
        
        return number