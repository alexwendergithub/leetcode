#nao notei que estava ordenado, dava pra fazer uma busca binaria
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        answer = None
        target = ord(target)
        for letter in letters:
            if ord(letter)>target:
                if answer == None:
                    answer = ord(letter)
                else:
                    if ord(letter)<answer:
                        answer = ord(letter)
        if answer != None:
            return chr(answer)
        else:
            return letters[0]