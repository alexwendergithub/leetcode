class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        skip = False
        soma = 0
        for num in nums:
            if not skip:
                soma+=num
            skip = not skip
        return soma