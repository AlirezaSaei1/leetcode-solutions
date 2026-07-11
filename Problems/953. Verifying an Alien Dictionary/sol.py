class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}

        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False

        return True
