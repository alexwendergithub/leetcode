class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        biggestSequence = 1
        currentSequence = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                currentSequence+=1
            else:
                biggestSequence = max(biggestSequence,currentSequence)
                currentSequence=1
        return max(biggestSequence,currentSequence)