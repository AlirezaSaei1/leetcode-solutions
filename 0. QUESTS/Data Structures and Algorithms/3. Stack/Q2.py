# V1

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}

        for token in tokens:
            if token in ops:
                second = stack.pop()
                first = stack.pop()
                result = 0

                if token == '+':
                    result = first + second
                elif token == '-':
                    result = first - second
                elif token == '*':
                    result = first * second
                else:
                    result = int(first / second)
                
                stack.append(result)
            else:
                stack.append(int(token))
                
        return stack.pop()
                

# V2

import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }

        for token in tokens:
            if token in ops:
                second = stack.pop()
                first = stack.pop()
                stack.append(ops[token](first, second))
            else:
                stack.append(int(token))
                
        return stack.pop()