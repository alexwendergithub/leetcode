class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        dif = 0
        def isPalindrome(left,right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        if len(s)<=2:
            return True
        while start<end:
            if s[start] == s[end]:
                start+=1
                end-=1
            else:
                return isPalindrome(start, end - 1) or isPalindrome(start + 1, end)
        return True