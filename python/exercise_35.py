class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = 0
        while n < len(nums):
            if nums[n]<target:
                n = n+1
            else:
                return n
        return n