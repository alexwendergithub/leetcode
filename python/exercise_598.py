#salvar os valores nao era necessario, so precisava achar o minimo op[0] e op[1]
import numpy as np

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        values = np.zeros((m, n))
        for op in ops:
            for i in range(op[0]):
                values[i][0]+=1
            for j in range(op[1]):
                if j == 0:
                    continue
                values[0][j]+=1
        print(values)
        countm = 0
        countn = 0
        for i in range(len(values)):
            if values[i][0] == values[0][0]:
                countn +=1
        for j in range(len(values[0])):
            if values[0][j] == values[0][0]:
                countm +=1
            else:
                break
        return countm*countn