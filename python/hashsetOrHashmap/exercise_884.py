from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        wordCountS1 = Counter(s1.split(" "))
        wordCountS2 = Counter(s2.split(" "))
        for word,count in wordCountS1.items():
            if word not in wordCountS2 and count == 1:
                res.append(word)
        for word,count in wordCountS2.items():
            if word not in wordCountS1 and count == 1:
                res.append(word)
        return res