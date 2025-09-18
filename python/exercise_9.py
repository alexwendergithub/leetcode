#se n fosse python utilizaria dois ponteiros
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]