class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        val_idx = defaultdict(list)
        for i, n in enumerate(nums):
            val_idx[n].append(i)
        
        n = len(nums)
        arr = [0] * n

        for i, n in enumerate(nums):
            indices = val_idx[n]
            if len(indices) < 1:
                continue
            else:
                res = 0
                for idx in indices:
                    if idx == i:
                        continue
                    else:
                        res += abs(i - idx)
                arr[i] = res

        return arr 

