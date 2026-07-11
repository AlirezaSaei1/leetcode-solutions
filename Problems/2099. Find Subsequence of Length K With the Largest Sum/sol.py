class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        imap = defaultdict(list)
        for i in range(n):
            imap[nums[i]].append(i)

        sorted_keys = sorted(imap.keys(), reverse=True)
        
        chosen_indices = []
        count = 0
        
        for val in sorted_keys:
            if count >= k:
                break
            
            indices = imap[val]
            for idx in indices:
                if count < k:
                    chosen_indices.append(idx)
                    count += 1
                else:
                    break
        
        chosen_indices.sort()
        return [nums[idx] for idx in chosen_indices]