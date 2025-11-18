class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        s = s+'I'
        left = 0
        right = len(s)-1
        for i in range(len(s)):
            if s[i] == "I":
                res.append(left)
                left+=1
            elif s[i] == "D":
                res.append(right)
                right-=1
        return res