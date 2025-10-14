#basicamente o mesmo que o 326
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 4:
            return False
        while n%4 == 0:
            n = n//4
        return n == 1