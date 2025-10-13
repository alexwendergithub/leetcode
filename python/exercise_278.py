# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        left = 1
        right = n
        fisrtBad = n
        lastGood = 1
        while left < right:
            middle = (left+right)//2
            versionBad = isBadVersion(middle)
            if versionBad == True:
                right = middle
            else:
                left = middle+1
        return left
