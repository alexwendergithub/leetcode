#no string manipulation, basically an array
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        currentLetter = ""
        groupSize = 0
        start = 0
        for i in range(len(s)):
            if currentLetter != s[i]:
                if groupSize>=3:
                    res.append([start,i-1])
                currentLetter = s[i]
                groupSize = 1
                start = i
            else:
                groupSize+=1
        if groupSize>=3:
            res.append([start,len(s)-1])

        return res