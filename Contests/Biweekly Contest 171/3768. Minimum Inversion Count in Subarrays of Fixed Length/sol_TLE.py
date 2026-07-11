class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        subarrays = []
        n = len(nums)

        def inversions(subarr, minn):
            count = 0
            for i in range(k):
                for j in range(i, k):
                    if subarr[i] > subarr[j]:
                        count += 1

                    if count > minn:
                        return float('inf')

            return count

        for i in range(0, n - k + 1):
            subarrays.append(nums[i:i+k])

        minn = float('inf')
        for sub in subarrays:
            count = inversions(sub, minn)
            if count == 0:
                return 0
            
            if minn > count:
                minn = count

        return minn