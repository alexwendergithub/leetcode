class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [-1]*len(s)
        leftE,rightE = None,None
        for i in range(len(s)):
            if s[i] == c:
                leftE = i
            if res[i] == -1 and leftE != None:
                res[i]= abs(leftE-i)
            elif res[i] != -1 and leftE != None:
                res[i] = min(res[i],abs(leftE-i))

            if s[len(s)-i-1] == c:
                rightE = len(s)-i-1
            if res[len(s)-i-1] == -1 and rightE != None:
                res[len(s)-i-1] = abs(rightE-(len(s)-i-1))
            elif res[len(s)-i-1] != -1 and rightE != None:
                res[len(s)-i-1] = min(res[len(s)-i-1],abs(rightE-(len(s)-i-1)))
        return res