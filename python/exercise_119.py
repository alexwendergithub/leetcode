class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = []
        for i in range(rowIndex+1):
            for j in range(i+1):
                print(j)
                if(j == 0):
                    a.append([1])
                elif(j == i):
                    a[i].append(1)
                else:
                    a[i].append(a[i-1][j-1]+a[i-1][j])
        return a[rowIndex]