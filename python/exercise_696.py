class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prevs = None
        prevCount = 0
        subCount = 0
        currentCount = 0
        for num in s:
            if num == '0':
                if  prevs == '1':
                    prevCount = currentCount
                    currentCount=1
                    subCount+=1
                    prevCount-=1
                else:
                    currentCount+=1
                    if prevCount:
                        prevCount-=1
                        subCount+=1
                prevs = '0'
            if num == '1':
                if  prevs == '0':
                    prevCount = currentCount
                    currentCount=1
                    subCount+=1
                    prevCount-=1
                else:
                    currentCount+=1
                    if prevCount:
                        prevCount-=1
                        subCount+=1
                prevs = '1'
        return subCount