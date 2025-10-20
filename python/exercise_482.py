class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        count = 0
        res = ""
        for letter in s[::-1]:
            if letter == "-":
                continue
            else:
                if count == k:
                    count = 0
                    res = letter+"-"+res
                    count+=1
                else:
                    count+=1
                    res = letter+res
        return res.upper()