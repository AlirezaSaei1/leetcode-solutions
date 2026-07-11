class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores_sorted = sorted(score, reverse=True)
        hashmap = {}

        for i, sc in enumerate(scores_sorted):
            if i == 0:
                hashmap[sc] = 'Gold Medal'
            elif i == 1:
                hashmap[sc] = 'Silver Medal'
            elif i == 2:
                hashmap[sc] = 'Bronze Medal'
            else:
                hashmap[sc] = str(i+1)
        
        return [hashmap[s] for s in score]


