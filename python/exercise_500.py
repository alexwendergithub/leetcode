class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiopQWERTYUIOP"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM"
        row = 0
        res = []
        for word in words:
            if word[0] in row1:
                row = 1
            elif word[0] in row2:
                row = 2
            elif word[0] in row3:
                row = 3
            if row == 1:
                rowset = row1
            elif row == 2:
                rowset = row2
            elif row == 3:
                rowset = row3
            else:
                continue
            rowdable = True
            for letter in word:
                if letter not in rowset:
                    rowdable = False    
            if rowdable:
                res.append(word)
        return res