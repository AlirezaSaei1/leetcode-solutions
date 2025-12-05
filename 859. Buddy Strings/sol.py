class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        idx = None

        for i in range(len(s)):
            if s[i] != goal[i]:
                if idx is not None:  
                    s_list = list(s)
                    s_list[idx], s_list[i] = s_list[i], s_list[idx]
                    return "".join(s_list) == goal
                else:
                    idx = i

        if idx is None:
            return len(set(s)) < len(s)

        return False
