class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = 0
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                for q in range(j+1, n):
                    x1,y1 = points[i]
                    x2,y2 = points[j]
                    x3,y3 = points[q]
                    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    if area>maxArea:
                        maxArea = area
        return maxArea