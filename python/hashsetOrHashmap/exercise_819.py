import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\b\w+\b', paragraph.lower())
        hashMap = {}
        for word in words:
            if word not in banned:
                if word in hashMap:
                    hashMap[word]+=1
                else:
                    hashMap[word]=1
        wordCount = 0
        biggestWord = ""
        for word in hashMap.keys():
            if hashMap[word] > wordCount:
                biggestWord = word
                wordCount = hashMap[word]
        return biggestWord