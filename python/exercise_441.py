class Solution:
    def arrangeCoins(self, n: int) -> int:
        counter = 1
        while n>0:
            n-=counter
            counter+=1
        if n==0:
            counter+=1
        return counter-2