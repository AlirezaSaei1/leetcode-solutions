class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        
        row = [1, 1]

        for i in range(1, rowIndex):
            temp = [1]
            for j in range(len(row)-1):
                temp.append(row[j] + row[j+1])
            temp.append(1)
            row = temp
        
        return row

