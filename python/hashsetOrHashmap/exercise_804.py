class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        wordsMorse = []
        count = 0
        for word in words:
            wordMorse = ''
            for letter in word:
                wordMorse += letters[(ord(letter) - 97)]
            if wordMorse in wordsMorse:
                continue
            else:
                wordsMorse.append(wordMorse)
                count+=1
        return count