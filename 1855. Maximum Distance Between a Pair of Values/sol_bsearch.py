class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def bsearch(arr, val, start):
            left = start
            right = len(arr) - 1
            best = 0

            while left <= right:
                mid = (left + right) // 2

                if val <= arr[mid]:
                    best = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
            return best - start

        answer = 0
        for i, num in enumerate(nums1):
            answer = max(answer, bsearch(nums2, num, i))
        
        return answer