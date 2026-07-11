class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        all_alice = sum(aliceSizes)
        all_bob = sum(bobSizes)

        diff = all_alice - all_bob

        target = diff // 2
        bob_set = set(bobSizes)

        for x in aliceSizes:
            y = x - target
            if y in bob_set:
                return [x, y]