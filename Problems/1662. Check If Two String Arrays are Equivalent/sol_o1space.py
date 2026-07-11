class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i = j = 0  # word1 chunk index, char index
        p = q = 0  # word2 chunk index, char index

        while i < len(word1) and p < len(word2):
            if j == len(word1[i]):
                i += 1
                j = 0
                continue
            if q == len(word2[p]):
                p += 1
                q = 0
                continue

            if word1[i][j] != word2[p][q]:
                return False

            j += 1
            q += 1

        while i < len(word1) and j == len(word1[i]):
            i += 1
            j = 0
        while p < len(word2) and q == len(word2[p]):
            p += 1
            q = 0

        return i == len(word1) and p == len(word2)
