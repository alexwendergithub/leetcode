#could have used a set with letter to value and just increase/decrease based on the next letter, but wanted to test how this would do compared to that

class Solution:
    def romanToInt(self, s: str) -> int:
        finalNumber = 0
        lastLetter = 0
        for letter in s:
            if letter == "V":
                if lastLetter == "I":
                    finalNumber = finalNumber+3
                else:
                    finalNumber = finalNumber+5
                lastLetter = "V"
            elif letter == "X":
                if lastLetter == "I":
                    finalNumber = finalNumber+8
                else:
                    finalNumber = finalNumber+10
                lastLetter = "X"
            elif letter == "L":
                if lastLetter == "X":
                    finalNumber = finalNumber+30
                else:
                    finalNumber = finalNumber+50
                lastLetter = "L"
            elif letter == "C":
                if lastLetter == "X":
                    finalNumber = finalNumber+80
                else:
                    finalNumber = finalNumber+100
                lastLetter = "C"
            elif letter == "D":
                if lastLetter == "C":
                    finalNumber = finalNumber+300
                else:
                    finalNumber = finalNumber+500
                lastLetter = "D"
            elif letter == "M":
                if lastLetter == "C":
                    finalNumber = finalNumber+800
                else:
                    finalNumber = finalNumber+1000
                lastLetter = "M"
            elif letter == "I":
                lastLetter = "I"
                finalNumber = finalNumber+1
        return finalNumber