class Solution:
    def checkRecord(self, s: str) -> bool:
        Acount = 0
        Lcount = 0
        for letter in s:
            if letter == 'A':
                Acount += 1
                if Acount >= 2:
                    return False
            if letter == 'L':
                Lcount+=1
                if Lcount >= 3:
                    return False
            else:
                if Lcount>0:
                    Lcount = 0
        return True