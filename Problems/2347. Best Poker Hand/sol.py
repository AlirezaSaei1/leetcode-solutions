class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        deck = Counter(ranks)
        rank_max = max(deck.values())
        if len(set(suits)) == 1:
            return 'Flush'
        elif 3 <= rank_max:
            return 'Three of a Kind'
        elif 2 == rank_max:
            return 'Pair'
        else:
            return 'High Card'
        
