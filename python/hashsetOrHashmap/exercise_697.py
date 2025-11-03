class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hashCount = {}
        hashCountSequence = {}
        firstAppearance = {}
        lastAppearance = {}
        lastElement = None
        currentSequence = 0
        count = 0
        for num in nums:
            if num in hashCount:
                lastAppearance[num]=count
                hashCount[num]+=1
                if lastElement != num:
                    currentSequence=1
                else:
                    currentSequence+=1
                if currentSequence>hashCountSequence[num]:
                    hashCountSequence[num] = currentSequence
            else:
                hashCount[num]=1
                hashCountSequence[num]=1
                currentSequence=1
                firstAppearance[num]=count
                lastAppearance[num]=count
            lastElement=num
            count+=1
        currentSequence = 0
        max_number = max(hashCount, key=hashCount.get)
        biggestSequence = 0
        longest = 0
        for num in hashCount:
            if hashCount[num]>longest:
                biggestSequence = lastAppearance[num]-firstAppearance[num]
                longest = hashCount[num]
            elif hashCount[num]==longest:
                biggestSequence = min(biggestSequence,lastAppearance[num]-firstAppearance[num])
        return biggestSequence+1