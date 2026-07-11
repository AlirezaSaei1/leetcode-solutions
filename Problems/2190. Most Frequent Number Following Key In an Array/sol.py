class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counts = Counter()

        for i in range(len(nums) - 1):
            if nums[i] == key:
                target = nums[i + 1]
                counts[target] += 1
        
        return counts.most_common(1)[0][0]