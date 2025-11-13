class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        shadowCount = 0
        for i in range(len(grid)):
            shadowCount+=max(grid[i])
            for j in range(len(grid[0])):
                if grid[i][j] >= 1:
                    shadowCount+=1
        for j in range(len(grid[0])):
            maxShadowCol = 0
            for i in range(len(grid)):
                if grid[i][j]>maxShadowCol:
                    maxShadowCol = grid[i][j]
            shadowCount+=maxShadowCol
        return shadowCount