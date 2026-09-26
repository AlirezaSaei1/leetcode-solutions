class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dict_k = {k: v for k, v in knowledge}
        res = []
        in_bracket = False
        curr_key = []

        for ch in s:
            if ch == '(':
                in_bracket = True
            elif ch == ')':
                in_bracket = False
                key_str = "".join(curr_key)
                res.append(dict_k.get(key_str, "?"))
                curr_key = []
            elif in_bracket:
                curr_key.append(ch)
            else:
                res.append(ch)

        return "".join(res)