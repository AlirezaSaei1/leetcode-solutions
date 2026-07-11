class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        balance = 0
        n = len(s) // 2

        for i in range(n):
            if s[i] in vowels:
                balance += 1
            if s[i + n] in vowels:
                balance -= 1

        return balance == 0
