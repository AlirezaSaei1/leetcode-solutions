class Solution:
    def minimumDeletions(self, s: str) -> int:
        counter = Counter(s)
        a_on_right = counter['a']
        b_on_left = 0

        min_cost = a_on_right

        for ch in s:
            if ch == 'a':
                a_on_right -= 1
            else:
                b_on_left += 1

            min_cost = min(min_cost, b_on_left + a_on_right)

        return min_cost
