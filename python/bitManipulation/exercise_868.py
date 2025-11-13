class Solution:
    def binaryGap(self, n: int) -> int:
        lastFound = -1
        count = 0
        distance = 0
        while n != 0:
            if n & 1:
                if lastFound != -1:
                    distance = max(count-lastFound,distance)
                lastFound = count
            count+=1
            n = n >> 1
        return distance