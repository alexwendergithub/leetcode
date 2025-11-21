class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in reversed(range(2,len(nums))):
            if nums[i-1]+nums[i-2]>nums[i]:
                return nums[i-1]+nums[i-2]+nums[i]
        return 0