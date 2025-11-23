class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""

        strs.sort()

        for i in range(len(strs[0])):
            if (strs[0][i] == strs[-1][i]):
                common+=strs[0][i]
            else:
                break

        return common