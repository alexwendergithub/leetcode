class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        previous = 0
        poison = 0
        for i in range(len(timeSeries)):
            if i == len(timeSeries)-1:
                poison+=duration
            elif timeSeries[i+1] == timeSeries[i]:
                continue
            elif timeSeries[i+1]-timeSeries[i] < duration:
                poison+=timeSeries[i+1]-timeSeries[i]
            else:
                poison+=duration
        return poison