import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2: return False
        sum_of_divisors = 1
        for i in range(2,int(math.sqrt(num)+1)):
            if num % i == 0:
                sum_of_divisors+=i
                if i*i != num:
                    sum_of_divisors+= num//i
        print(sum_of_divisors)
        return num == sum_of_divisors