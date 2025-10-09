class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        a = list(str(n))
        print(a)
        results = []
        while sum != 1:
            sum = 0
            for num in a:
                sum += int(num)*int(num)
            print(sum)
            a = list(str(sum))
            if sum in results:
                return False
            results.append(sum)
        return True