class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_selfdividing(num):
            temp = num
            
            while temp > 0:
                digit = temp % 10

                if digit == 0:
                    return False
                
                if not num % digit == 0:
                    return False
                
                temp //= 10
            
            return True

        result = []
        for i in range(left, right+1):
            if is_selfdividing(i):
                result.append(i)
        
        return result