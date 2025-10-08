class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column = ""
        charachterList = ['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        while columnNumber>26:
            num = columnNumber%26
            columnNumber = int(columnNumber/26)
            if num == 0:
                columnNumber = columnNumber-1
            column = charachterList[num]+column

        print(columnNumber)
        print(charachterList)
        print(charachterList[columnNumber])
        print(column)
        return charachterList[columnNumber]+column