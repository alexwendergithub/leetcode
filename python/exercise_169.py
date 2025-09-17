class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bigNumber = 0
        count = 0
        for num in nums:
            if count == 0:
                bigNumber = num
            if num == bigNumber:
                count=count+1
            else:
                count = count-1
        return bigNumber