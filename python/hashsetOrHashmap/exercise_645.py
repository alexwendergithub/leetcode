class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashMap = {}
        duplicate = None
        soma = 0
        for num in nums:
            if num in hashMap:
                duplicate = num
            else:
                hashMap[num]=1
            soma+=num
        return [duplicate,int((len(nums)*(len(nums)+1))/2) - (soma-duplicate)]