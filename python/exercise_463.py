#fazer com algum algoritimo de busca depois
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        per = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i-1 < 0:
                        per+=1
                    else:
                        if not grid[i-1][j]:
                            per+=1
                    if j-1 < 0:
                        per+=1
                    else:
                        if not grid[i][j-1]:
                            per+=1
                    if i+1 >= len(grid):
                        per+=1
                    else:
                        if not grid[i+1][j]:
                            per+=1
                    if j+1 >= len(grid[i]):
                        per+=1
                    else:
                        if not grid[i][j+1]:
                            per+=1
        return per