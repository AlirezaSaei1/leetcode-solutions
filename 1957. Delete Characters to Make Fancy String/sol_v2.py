class Solution:
    def makeFancyString(self, s: str) -> str:
        answer = []
        
        for char in s:
            if len(answer) >= 2 and answer[-1] == char and answer[-2] == char:
                continue

            answer.append(char)
            
        return "".join(answer)