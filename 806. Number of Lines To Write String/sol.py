class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        cur_width = 0

        for char in s:
            w = widths[ord(char) - ord('a')]
            if cur_width + w > 100:
                lines += 1
                cur_width = 0
            cur_width += w
        
        return [lines, cur_width]