class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        surfaceArea=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    surfaceArea+=2
                    if i-1 == -1:
                        surfaceArea+=grid[i][j]
                    elif grid[i][j]>grid[i-1][j]:
                        surfaceArea+=grid[i][j]-grid[i-1][j]
                    if i+1 == len(grid):
                        surfaceArea+=grid[i][j]
                    elif grid[i][j]>grid[i+1][j]:
                        surfaceArea+=grid[i][j]-grid[i+1][j]
                    if j-1 == -1:
                        surfaceArea+=grid[i][j]
                    elif grid[i][j]>grid[i][j-1]:
                        surfaceArea+=grid[i][j]-grid[i][j-1]
                    if j+1 == len(grid[0]):
                        surfaceArea+=grid[i][j]
                    elif grid[i][j]>grid[i][j+1]:
                        surfaceArea+=grid[i][j]-grid[i][j+1]
        return surfaceArea