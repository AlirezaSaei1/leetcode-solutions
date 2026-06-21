class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort(reverse=True)
        count = 0

        while costs:
            c = costs.pop()
            if coins - c >= 0:
                count += 1
                coins -= c
            else:
                break
        
        return count