class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        answer = []

        for query in queries:
            for word in dictionary:
                count = 0
                for ch1, ch2 in zip(query, word):
                    if ch1 != ch2:
                        count += 1
                    
                    if count > 2:
                        break
                else:
                    answer.append(query)
                    break
        
        return answer