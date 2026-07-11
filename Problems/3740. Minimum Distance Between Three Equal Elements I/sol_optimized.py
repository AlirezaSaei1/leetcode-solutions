class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Step 1: Group all indices for each number
        val_to_indices = defaultdict(list)
        for idx, val in enumerate(nums):
            val_to_indices[val].append(idx)

        min_dist = float('inf')

        # Step 2: Iterate through each group
        for indices in val_to_indices.values():
            if len(indices) < 3:
                continue
            
            # Step 3: Check only consecutive triplets
            # The distance for i < j < k is always 2 * (k - i)
            for m in range(len(indices) - 2):
                # indices[m] is our 'i', indices[m+2] is our 'k'
                current_dist = 2 * (indices[m + 2] - indices[m])
                if current_dist < min_dist:
                    min_dist = current_dist

        return min_dist if min_dist != float('inf') else -1