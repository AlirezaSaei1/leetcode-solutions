class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        answer = sum(technique2)
        n = len(technique1)
        diffs = [t1 - t2 for t1, t2 in zip(technique1, technique2)]
        diffs.sort(reverse=True)

        answer += sum(diffs[:k])
        
        for diff in diffs[k:]:
            if diff > 0:
                answer += diff
            else:
                break

        return answer