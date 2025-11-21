class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        index = len(num)-1
        while index >= 0 or k > 0:       
            if index >= 0:
                k += num[index]
            carry, digit = divmod(k, 10)
            res.append(digit)
            k = carry
            index -= 1
        return res[::-1]