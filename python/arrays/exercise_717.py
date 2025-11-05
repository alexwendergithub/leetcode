class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)<2:
            return True
        if bits[-1] == 0 and bits[-2] == 0:
            return True
        pointera = 0
        while pointera<len(bits):
            if pointera == len(bits)-2:
                return False
            elif pointera == len(bits)-1:
                return True
            if bits[pointera] == 1:
                pointera+=2
            else:
                pointera+=1
        return False