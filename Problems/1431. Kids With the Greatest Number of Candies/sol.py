class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        kids = len(candies)
        maxx = max(candies)
        bool_arr = [False] * kids

        for i in range(kids):
            if candies[i] + extraCandies >= maxx:
                bool_arr[i] = True
        
        return bool_arr