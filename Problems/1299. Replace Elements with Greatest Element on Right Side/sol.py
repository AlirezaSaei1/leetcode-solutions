class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = arr[-1]
        n = len(arr)
        ans = [-1]

        for i in range(n - 2, -1, -1):
            ans.append(maxx)
            if maxx < arr[i]:
                maxx = arr[i]

        ans.reverse()
        return ans
