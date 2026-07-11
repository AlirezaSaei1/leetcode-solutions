class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(num):
            if num <= 1:
                return False

            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    return False

            return True


        # prefix
        str_num = str(num)
        n = len(str_num)
        for i in range(1, n):
            if not is_prime(int(str_num[:i])):
                #print(int(str_num[:i]))
                return False

        # suffix
        for i in range(n-1, -1, -1):
            if not is_prime(int(str_num[i:])):
                #print(int(str_num[i:]))
                return False

        return True