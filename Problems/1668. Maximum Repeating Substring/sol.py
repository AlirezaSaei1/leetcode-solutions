class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        max_k = 0

        for i in range(n):
            cur_k = 0
            j = i
            while j + m <= n and sequence[j:j+m] == word:
                cur_k += 1
                j += m
            max_k = max(max_k, cur_k)

        return max_k