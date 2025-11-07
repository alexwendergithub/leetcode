class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels ="aeiouAEIOU"
        words = sentence.split(" ")
        count = 1
        res = []
        for word in words:
            count +=1
            if word[0] in vowels:
                word = word+"m"+('a'*count)
            else:
                word = word[1:]+word[0]+"m"+('a'*count)
            res.append(word)
        return  " ".join(res)