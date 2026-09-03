class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2 != 0:
                if x < min_odd:
                    min_odd = x
            else:
                if x < min_even:
                    min_even = x

        can_make_odd = True
        if min_even != float('inf'):
            if min_even < min_odd:
                can_make_odd = False

        can_make_even = True
        if min_odd != float('inf'):
            can_make_even = False

        return can_make_odd or can_make_even