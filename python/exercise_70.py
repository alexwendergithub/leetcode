#could have made recurssion with a list saving the returns for n as well

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        num0 = 1
        num1 = 1
        for num in range(n):
            num2 = num0+num1
            num0 = num1
            num1 = num2
        return num0