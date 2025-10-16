class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        res = []
        currentValue = nums[0]
        rangeStart = 0 
        for i in range(len(nums)):
            if i == 0:
                continue
            if not (nums[i] == (nums[i-1]+1)):
                if rangeStart != i-1:
                    res.append(str(nums[rangeStart])+"->"+str(nums[i-1]))
                else:
                    res.append(str(nums[i-1]))
                rangeStart = i
            if i == len(nums)-1:
                print(rangeStart)
                if rangeStart == i:
                    res.append(str(nums[i]))
                else:
                    res.append(str(nums[rangeStart])+"->"+str(nums[i]))
        return res