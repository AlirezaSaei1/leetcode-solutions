class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def valid_code(s):
            return s != "" and all(c.isalnum() or c == '_' for c in s)

        valid_lines = {"electronics", "grocery", "pharmacy", "restaurant"}
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        valid = []
        for i in range(len(code)):
            if isActive[i] and businessLine[i] in valid_lines and valid_code(code[i]):
                valid.append((order[businessLine[i]], code[i]))

        valid.sort()
        return [c for _, c in valid]
