class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        valid_intervals = []

        for ch in set(s):
            left = first[ch]
            right = last[ch]
            is_valid = True

            i = left
            while i <= right:
                c = s[i]
                if first[c] < left:
                    is_valid = False
                    break
                right = max(right, last[c])
                i += 1

            if is_valid:
                valid_intervals.append((right, left))

        valid_intervals.sort()

        ans = []
        prev_end = -1

        for right, left in valid_intervals:
            if left > prev_end:
                ans.append(s[left : right + 1])
                prev_end = right

        return ans