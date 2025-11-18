class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        count = {}
        for num in nums:
            if num in count:
                return num
            else:
                count[num]=1
        return -1