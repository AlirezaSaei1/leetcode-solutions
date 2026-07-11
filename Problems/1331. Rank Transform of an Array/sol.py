class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))
        rank = {num: i + 1 for i, num in enumerate(temp)}
        return [rank[i] for i in arr]