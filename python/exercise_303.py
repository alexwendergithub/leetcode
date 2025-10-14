#poderia salvar os resultados num array pra otimizar runtime
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        soma = 0
        for i in range(left,right+1):
            soma += self.nums[i]
        return soma


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)