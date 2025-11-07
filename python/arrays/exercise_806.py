class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lineCount = 1
        widthCount = 0
        for letter in s:
            widthCount += widths[ord(letter)-97]
            if widthCount>100:
                widthCount = widths[ord(letter)-97]
                lineCount+=1
        return [lineCount,widthCount]