class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []

        for j in range(numRows):
            if j == 0:
                row = [1]
            else: 
                row = [1]
                last_row = pascal[-1]
                for i in range(len(last_row)-1):
                    row.append(last_row[i] + last_row[i+1])
                row.append(1)
            pascal.append(row)
        
        return pascal