from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)  
        maxCount = 0
        for item, count in counter.items():
            if counter[item+1]>0:
                if counter[item+1]+count>maxCount:
                    maxCount=counter[item+1]+count
        return maxCount