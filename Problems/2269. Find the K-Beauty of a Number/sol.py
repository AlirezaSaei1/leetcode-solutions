class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numstr = str(num)
        count = 0

        for i in range(len(numstr) - k + 1):
            number = int(numstr[i:i+k])
            if number != 0 and num % number == 0:
                count += 1
        
        return count