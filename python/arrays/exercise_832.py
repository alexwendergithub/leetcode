class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped_matrix = []
        for row in image:
            flipped_matrix.append(row[::-1]) 
        for i in range(len(flipped_matrix)):
            for j in range(len(flipped_matrix[0])):
                flipped_matrix[i][j]=flipped_matrix[i][j]^1
        return flipped_matrix