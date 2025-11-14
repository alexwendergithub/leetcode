class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increassing = False
        decreassing = False
        prevNum = nums[0]
        for num in nums:
            if num>prevNum and decreassing:
                return False
            if num<prevNum and increassing:
                return False
            if num>prevNum:
                increassing = True
            if num<prevNum:
                decreassing = True
            prevNum = num
        return True