class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lastEven = 0
        for i in range(len(nums)):
            if not nums[i]%2:
                nums[i],nums[lastEven] = nums[lastEven],nums[i]
                lastEven+=1
        return nums