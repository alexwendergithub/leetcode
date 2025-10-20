class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        first = None
        second = None
        third = None
        for num in nums:
            if num == first or num == second or num == third:
                continue
            if first == None or num > first:
                third = second
                second = first
                first = num
            elif second == None or num > second:
                third = second
                second = num
            elif third == None or num > third:
                third = num

        if third != None:
            return third
        else:
            return first