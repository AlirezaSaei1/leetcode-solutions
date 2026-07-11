class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)

        count_n = Counter(nums)
        count_f = Counter(forbidden)
        for key in count_n:
            cntn = count_n[key]
            cntf = count_f[key]
            if cntn + cntf > n:
                return -1
        
        bad = []
        for i in range(n):
            if nums[i] == forbidden[i]:
                bad.append(nums[i])

        b = len(bad)
        if b == 0:
            return 0

        bad_freq = Counter(bad)
        max_freq = max(bad_freq.values())

        if max_freq > b//2:
            p = b - max_freq
        else:
            p = b // 2
            
        return b - p
            
        # swaps = 0
        # swap_idx = []
        # bad_n = len(bad)
        # for i in range(bad_n):
        #     ii = bad[i]
        #     if ii in swap_idx:
        #         continue
        #     for j in range(i + 1, bad_n):
        #         jj = bad[j]
        #         if jj in swap_idx:
        #             continue
        #         if nums[ii] != forbidden[jj] and nums[jj] != forbidden[ii]:
        #             swaps += 1
        #             swap_idx.append(ii)
        #             swap_idx.append(jj)
        #             break

        # for i in range(0, len(swap_idx), 2):
        #     nums[i], nums[i+1] = nums[i+1], nums[i]

        # bad2 = []
        # for i in range(n):
        #     if nums[i] == forbidden[i]:
        #         bad2.append(i)

        # for bd in bad2:
        #     for i in range(n):
        #         if i == bd:
        #             continue
        #         if nums[i] != forbidden[bd] and forbidden[i] != nums[bd]:
        #             swaps += 1
        #             break
        
        # return swaps
        
        