class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        left = 0
        right = 1
        while left<len(nums) and right<len(nums):
            if nums[left]%2 and not nums[right]%2:
                nums[left],nums[right] = nums[right],nums[left]
                left+=2
                right+=2
            else:
                if not nums[left]%2:
                    left+=2
                if nums[right]%2:
                    right+=2
        return nums