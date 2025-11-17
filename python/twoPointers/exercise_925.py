class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        pointerA = 0
        lastPressed = ''
        result = False
        for charachter in typed:
            if result == False and charachter == name[pointerA]:
                pointerA+=1
                lastPressed = charachter
                if pointerA == len(name):
                    result = True
            else:
                if charachter != lastPressed:
                    return False
        return result