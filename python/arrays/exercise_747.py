class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        biggestNum = -1
        secondBiggestNum = -1
        count = 0
        index = 0
        for num in nums:
            if biggestNum == -1:
                biggestNum = num
                index = count
            elif secondBiggestNum == -1:
                if num > biggestNum:
                    secondBiggestNum = biggestNum
                    biggestNum = num
                    index = count
                else:
                    secondBiggestNum = num
            elif num >= biggestNum:
                index = count
                secondBiggestNum = biggestNum
                biggestNum = num
            elif num > secondBiggestNum:
                secondBiggestNum = num
            count+=1
        if biggestNum >= secondBiggestNum*2:
            return index
        else:
            return -1