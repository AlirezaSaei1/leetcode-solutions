class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        def is_balanced(x):
            odd = 0
            even = 0
            i = 0

            while x:
                r = x % 10
                if i % 2 == 0:
                    odd += r
                else:
                    even += r
                i += 1
                x //= 10

            return odd == even
        
        count = 0
        start = low
        while start % 11 != 0:
            start += 1
        
        for i in range(start, high+1, 11):
            if is_balanced(i):
                count += 1
        
        return count