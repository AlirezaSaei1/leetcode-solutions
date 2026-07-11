class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        suffix_y = customers.count('Y')

        prefix_n = 0
        min_penalty = suffix_y
        earliest = 0

        for i, c in enumerate(customers):
            penalty = prefix_n + suffix_y
            if penalty < min_penalty:
                min_penalty = penalty
                earliest = i

            if c == 'Y':
                suffix_y -= 1
            else:
                prefix_n += 1

        if prefix_n < min_penalty:
            earliest = n

        return earliest
