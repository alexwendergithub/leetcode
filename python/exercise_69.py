class Solution:
    def mySqrt(self, x: int) -> int:
        currentNumber = 1
        nextNumber = 2
        if x == 0:
            return 0
        if x < 2:
            return 1
        while currentNumber*currentNumber <= x:
            currentNumber = currentNumber+1
        currentNumber = currentNumber-1
        return currentNumber