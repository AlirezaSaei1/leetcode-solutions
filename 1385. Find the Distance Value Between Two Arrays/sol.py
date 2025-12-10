class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        dist = 0

        for num in arr1:
            pos = bisect.bisect_left(arr2, num)
            ok = True
            if pos < len(arr2) and abs(arr2[pos] - num) <= d:
                ok = False
            if pos > 0 and abs(arr2[pos - 1] - num) <= d:
                ok = False
            
            if ok:
                dist += 1
        
        return dist
