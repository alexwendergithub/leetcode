class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        prime_list = [2,3,5,7,11,13,17,19]
        for num in range(left,right+1):
            bits = num.bit_count()
            if bits in prime_list:
                count+=1
        return count