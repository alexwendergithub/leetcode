#return word.isupper() or word.islower() or word.istitle()
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if not word[0].isupper() and word[1].isupper():
            return False
        firstup = False
        if word[0].isupper():
            firstup = True
        secondup = False
        if word[1].isupper():
            secondup = True
        if firstup:
            for letter in word[2:]:
                if not secondup and letter.isupper():
                    return False
                elif secondup and not letter.isupper():
                    return False        
        else:
            for letter in word[2:]:
                if letter.isupper():
                    return False
        return True
