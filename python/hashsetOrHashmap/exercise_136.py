class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for number in nums:
            if number not in hashMap:
                hashMap[number] = 1
            else:
                del(hashMap[number])
        return list(hashMap.keys())[0]