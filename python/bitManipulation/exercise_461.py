class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x^y
        print(a)
        counter = 0
        while a>0:
            if a & 1:
                counter+=1
            a = a >> 1
        return counter