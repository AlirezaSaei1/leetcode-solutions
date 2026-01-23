class Solution:
    def minOperations(self, s: str) -> int:
        var1, var2 = 0, 0
        n = len(s)

        # start 0
        for i in range(n):
            if i % 2 == 0:
                if s[i] == '1':
                    var1 += 1
            else:
                if s[i] == '0':
                    var1 += 1

        # start 1
        for i in range(n):
            if i % 2 == 0:
                if s[i] == '0':
                    var2 += 1
            else:
                if s[i] == '1':
                    var2 += 1
                
        return min(var1, var2)