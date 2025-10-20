class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentCount = 0
        maxCount = 0
        for num in nums:
            if num == 1:
                currentCount += 1
            if num == 0:
                if currentCount > maxCount:
                    maxCount = currentCount
                currentCount = 0
        if currentCount > maxCount:
            return currentCount
        return maxCount