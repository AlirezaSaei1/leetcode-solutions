class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1, p2 = len(s) - 1, len(t) - 1

        while p1 >= 0 or p2 >= 0:
            # process backspaces for s
            back1 = 0
            while p1 >= 0:
                if s[p1] == '#':
                    back1 += 1
                    p1 -= 1
                elif back1 > 0:
                    back1 -= 1
                    p1 -= 1
                else:
                    break   # s[p1] is a valid char

            # process backspaces for t
            back2 = 0
            while p2 >= 0:
                if t[p2] == '#':
                    back2 += 1
                    p2 -= 1
                elif back2 > 0:
                    back2 -= 1
                    p2 -= 1
                else:
                    break

            # now compare the current valid chars
            if p1 >= 0 and p2 >= 0:
                if s[p1] != t[p2]:
                    return False
            elif p1 >= 0 or p2 >= 0:
                # one string has chars left, the other doesn't
                return False

            p1 -= 1
            p2 -= 1

        return True
