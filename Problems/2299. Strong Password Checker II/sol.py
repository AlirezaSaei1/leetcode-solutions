class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n = len(password)

        if n < 8:
            return False

        flags = [False] * 4
        prev= None

        for i in range(n):
            char = password[i]

            if char.islower():
                flags[0] = True
            
            if char.isupper():
                flags[1] = True
            
            if char.isdigit():
                flags[2] = True
            
            if char in "!@#$%^&*()-+":
                flags[3] = True
            
            if prev == char:
                return False
            
            prev = char
        
        return all(flags)
