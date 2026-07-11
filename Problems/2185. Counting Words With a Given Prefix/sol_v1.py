class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answer = 0
        np = len(pref)

        for word in words:
            nw = len(word)
            for i in range(np):
                if i >= nw or word[i] != pref[i]:
                    break
            else:
                answer += 1

        return answer