class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        pointer_g = len(g)-1
        res = 0
        pointer_s = len(s)-1
        g.sort()
        s.sort()
        while pointer_g >= 0 and pointer_s >= 0:
            if s[pointer_s] >= g[pointer_g]:
                res += 1
                pointer_g -= 1
                pointer_s -= 1
            else:
                pointer_g -= 1
        return res