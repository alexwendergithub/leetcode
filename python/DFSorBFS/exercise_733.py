class Solution:
    globalImage = None
    visited = []
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int,prevColor = None) -> List[List[int]]:
        originalColor = image[sr][sc]
        if originalColor == color:
            return image
        rows = len(image)-1
        cols = len(image[0])-1
        def dfs(row,col):
            image[row][col] = color
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for rowchange,colchange in directions:
                if 0<=row+rowchange<=rows and 0<=col+colchange<=cols:
                    if image[row+rowchange][col+colchange] == originalColor:
                        dfs(row+rowchange,col+colchange)
        dfs(sr,sc)
        return image