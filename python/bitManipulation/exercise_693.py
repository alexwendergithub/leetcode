class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        alternate = n & 1
        while n != 0:
            if alternate:
                if not(n & 1):
                    return  False
            else:
                if (n & 1):
                    return False
            alternate = not alternate
            n = n >> 1
        return True