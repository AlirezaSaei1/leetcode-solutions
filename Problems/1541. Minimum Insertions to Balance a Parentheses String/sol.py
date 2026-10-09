class Solution:
    def minInsertions(self, s: str) -> int:
        needed_insertions = 0
        open_needed = 0

        for char in s:
            if char == '(':
                if open_needed % 2 != 0:
                    needed_insertions += 1
                    open_needed -= 1
                open_needed += 2
            else:
                open_needed -= 1
                if open_needed < 0:
                    needed_insertions += 1
                    open_needed += 2

        return needed_insertions + open_needed