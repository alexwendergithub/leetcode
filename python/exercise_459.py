class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s2 = s
        for i in range(int(len(s2)/2)):
            a = s[0]
            s = s[1:]+a
            if s == s2:
                return True

        return False