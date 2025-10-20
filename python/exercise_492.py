class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area < 4:
            return [area,1]
        results = []
        for i in range(1,int(sqrt(area))+1):
            if area%i == 0:
                results.append([int(area/i),i])
        return results[-1]