class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(idx: int):
            groups = []
            curr_group = [{""}]

            while idx < len(expression):
                ch = expression[idx]

                if ch == '{':
                    inner_set, next_idx = parse(idx + 1)
                    curr_group.append(inner_set)
                    idx = next_idx

                elif ch == '}':
                    groups.append(curr_group)
                    return evaluate(groups), idx + 1

                elif ch == ',':
                    groups.append(curr_group)
                    curr_group = [{""}]
                    idx += 1

                else:
                    curr_group.append({ch})
                    idx += 1

            groups.append(curr_group)
            return evaluate(groups), idx

        def evaluate(groups):
            total_set = set()
            for group in groups:
                res = {""}
                for s_set in group:
                    res = {a + b for a in res for b in s_set}
                total_set.update(res)
            return total_set

        res_set, _ = parse(0)
        return sorted(list(res_set))