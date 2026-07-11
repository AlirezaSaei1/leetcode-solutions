class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = set([p[0] for p in paths])
        ends = set([p[1] for p in paths])
        return (ends - starts).pop()