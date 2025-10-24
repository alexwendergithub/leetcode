class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not r*c == len(mat)*len(mat[0]):
            return mat
        row = len(mat)-1
        col = len(mat[0])-1
        counterrow = 0
        countercol = 0
        res = [[None for _ in range(c)] for _ in range(r)]
        for i in range(0,r):
            for j in range(0,c):
                res[i][j] = mat[counterrow][countercol]
                countercol+=1
                if countercol>col:
                    countercol = 0
                    counterrow+=1
        return res