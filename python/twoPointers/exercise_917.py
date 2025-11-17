class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s)-1
        s = list(s)
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while left<right:
            if s[left] in letters and s[right] in letters:
                s[left],s[right] = s[right],s[left]
                left+=1
                right-=1
            elif s[left] not in letters:
                left+=1
            elif s[right] not in letters:
                right-=1
        return ''.join(s)