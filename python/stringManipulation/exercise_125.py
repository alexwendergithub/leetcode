import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        print(s)
        pointerLast = len(s)-1
        for n in range(int(len(s)/2)):
            if s[n] != s[pointerLast-n]:
                return False
        return True