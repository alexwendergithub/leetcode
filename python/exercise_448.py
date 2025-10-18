class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = [0] * (len(nums)+1)
        res = []
        for num in nums:
            numbers[num] = 1

        for i in range(1,len(numbers)):
            if numbers[i] == 0:
                res.append(i)
        return res