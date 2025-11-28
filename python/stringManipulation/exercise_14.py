def compare(str1,str2):
    n=0
    for x, y in zip(str1,str2):
        print([x,y])
        if x == y:
            n=n+1
        if x !=y:
            break
    if n == 0:
        return ""
    else:
        return str1[:n]
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        common = strs[0]
        for word in strs[1:]:
            common = compare(word,common)
            if common == "":
                return ""
        return common